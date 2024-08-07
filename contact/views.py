from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


class ViewContact(View):

    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = form.cleaned_data.get('subject', '')
            message = form.cleaned_data.get('message', '')
            email_from = settings.EMAIL_HOST_USER
            recipient = [settings.EMAIL_HOST_USER]

            try:
                # Sending Email
                send_mail(subject, message, email_from, recipient)
                messages.success(
                    request, 'Your message has been sent successfully.')
            except Exception as e:
                messages.error(request, 'Error sending email: ' + str(e))

            return redirect('contact:contact')

        context = {'form': form}
        return render(request, 'contact.html', context)
