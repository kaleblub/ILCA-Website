from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
	return render(request, 'registration/register.html')

@login_required
def login(request):
	return render(request, 'registration/login.html')