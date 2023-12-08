from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import activate

# Create your views here.
def home(request):
	language = request.COOKIES.get('django_language', 'en')

	activate(language)

	return render(request, 'main/home.html')

def set_language(request, language):
	print(f"Language selected: {language}")

	redirect_url = reverse('home')
	# print(f"Redirect to: {response.url}")

	response = redirect(redirect_url)
	response.set_cookie('django_language', language)
	return response