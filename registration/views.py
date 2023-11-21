from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
def registration(request):
	return render(request, 'registration/register.html')


class CustomLoginView(LoginView):
	template_name = 'registration/login.html'

	def get_success_url(self):
		return super().get_success_url()

	def form_valid(self, form):
		return super().form_valid(form)

	def form_invalid(self, form):
		return super().form_invalid(form)