from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            #save to the database 
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )

            #sendd an email notification
            message_body = f"New job application received from {first_name} {last_name}. \
            \nEmail: {email}\nDate: {date}\nOccupation: {occupation}"
            email_message = EmailMessage(
                subject='Job Application Form Submitted Successfully',
                body=message_body,
                to=[email]
            )
            email_message.send()

            messages.success(request, 'Your application has been submitted successfully.')

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
