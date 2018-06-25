from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    response = User.objects.validateRegistration(request.POST)
    if 'errors' in response:
        for error in response['errors']:
            messages.error(request,error)
        return redirect('/')
    else:
        request.session['user_id'] = response['user_id']
        return redirect('/quotes/')
    