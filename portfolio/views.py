from datetime import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .models import Info, Project, Contact, Skill, Timeline
from .forms import ContactForm
from django.templatetags.static import static


def index(request):
    info = Info.objects.all()
    project = Project.objects.all().order_by('-project_date')
    skill = Skill.objects.all()
    timeline = Timeline.objects.all()
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
        'work': project, 
        'form': form, 
        'skill': skill,
        'timeline': timeline
        })
