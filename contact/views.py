from django.shortcuts import render
from .models import Contact
from django.contrib import messages


def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        messages.success(request, 'We received your message!')

    template = 'contact/contact.html'
    context = {
        'on_profile_page': True
    }

    return render(request, template, context)
