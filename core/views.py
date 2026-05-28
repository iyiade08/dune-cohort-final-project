from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == 'POST':
        messages.success(request, 'Thank you! We will get back to you shortly.')
        return redirect('/contact/')
    return render(request, 'core/contact.html')