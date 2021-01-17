from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .models import Info, Work,Contact
from .forms import ContactForm


def index(request):
    info = Info.objects.all()
    work = Work.objects.all()
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            contact = Contact(from_email=from_email, subject=subject, message=message)
            try:
                send_mail(subject, message, from_email, ['nattapol.boo@ku.th'], fail_silently=False)
                contact.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'portfolio/index.html', {'info': info, 'work': work, 'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

    
