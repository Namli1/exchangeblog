import requests
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import Permission
from blog import development_settings as settings
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView

from authentication.forms import SignUpWithCodeForm, PasswordResetFormWithReCaptcha

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpWithCodeForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_key"] = settings.RECAPTCHA_PUBLIC_KEY
        return context

    def form_valid(self, form):
        user = form.save()
        blogauthor_create_permission = Permission.objects.get(codename="add_blogauthor")
        user.user_permissions.add(blogauthor_create_permission)
        return super(SignUpView, self).form_valid(form)

class ReCaptchaPasswordResetView(PasswordResetView):
    form_class = PasswordResetFormWithReCaptcha

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_key"] = settings.RECAPTCHA_PUBLIC_KEY
        return context