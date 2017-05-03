from __future__ import absolute_import
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User

from .forms import RegistrationForm

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = 'main_app/home.html'

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'main_app/signup.html'