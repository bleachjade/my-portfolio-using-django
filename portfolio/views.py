from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .models import Info, Work, Contact
from .forms import ContactForm
from django.conf import settings

import os


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
                contact.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, f"Success! Thank you for your message.")
            return redirect('index')
    return render(request, 'portfolio/index.html', {'info': info, 'work': work, 'form': form})

def pdf_view(request):
    try:
        return FileResponse(open('portfolio/static/pdf/my_resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    
