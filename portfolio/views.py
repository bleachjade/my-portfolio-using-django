from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .models import Info, Work, Contact, Skill, InternshipWork, FreelanceWork, Activity
from .forms import ContactForm
from django.conf import settings
from django.templatetags.static import static

import os


def index(request):
    info = Info.objects.all()
    work = Work.objects.all().order_by('-project_date')
    skill = Skill.objects.all()
    intern_work = InternshipWork.objects.all().order_by('-project_date')
    freelance_work = FreelanceWork.objects.all().order_by('-project_date')
    activity = Activity.objects.all().order_by('-activity_date')
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
    return render(request, 'portfolio/index.html', {
        'info': info, 
        'work': work, 
        'form': form, 
        'skill': skill,
        'intern_work': intern_work,
        'freelance_work': freelance_work,
        'activity': activity
        })


    
