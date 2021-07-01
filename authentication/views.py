import requests
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.contrib.auth.models import Permission
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import ValidationError
from django.core.exceptions import PermissionDenied

from authentication.forms import SignUpWithCodeForm, PasswordResetFormWithReCaptcha, RegistrationCodeForm
from authentication.models import RegistrationCode

# Create your views here.

class SignUpView(UserPassesTestMixin, generic.CreateView):
    form_class = SignUpWithCodeForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_key"] = settings.RECAPTCHA_PUBLIC_KEY
        return context

    def test_func(self):
        try:
            if self.request.user.is_authenticated():
                raise PermissionDenied(_("You can't sign-up if you are already logged in :-)."))
            else:
                return True
        except:
            return True

    def form_valid(self, form):
        registration_code = form.cleaned_data.get('registration_code')
        if RegistrationCode.objects.filter(code=registration_code).first().code_exists_and_valid():
            user = form.save()
            used_code = RegistrationCode.objects.filter(code=registration_code).first()
            used_code.used_by = user
            used_code.save()
            if used_code.has_blogauthor_permission:
                blogauthor_create_permission = Permission.objects.get(codename="add_blogauthor")
                user.user_permissions.add(blogauthor_create_permission)
            if used_code.has_guidepost_permission:
                guidepost_create_permission = Permission.objects.get(codename="add_guidepost")
                user.user_permissions.add(guidepost_create_permission)
            if used_code.has_countryguide_permission:
                countryguide_create_permission = Permission.objects.get(codename="add_countryguidepost")
                user.user_permissions.add(countryguide_create_permission)
        else:
            print("hello")
            raise ValidationError(_("Invalid registration code. This code might not exist or is turned invalid. Please make sure you spelled it correctly. If it's not working, contact the admin via Instagram."), code='invalid')
        # blogauthor_create_permission = Permission.objects.get(codename="add_blogauthor")
        # user.user_permissions.add(blogauthor_create_permission)
        return super(SignUpView, self).form_valid(form)

class ReCaptchaPasswordResetView(PasswordResetView):
    form_class = PasswordResetFormWithReCaptcha

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_key"] = settings.RECAPTCHA_PUBLIC_KEY
        return context

class RegistrationCodeCreate(UserPassesTestMixin, generic.CreateView):
    model = RegistrationCode
    form_class = RegistrationCodeForm
    success_url = reverse_lazy('home')
    permission_denied_message = _('This page is only available to site admins')

    def test_func(self):
        return self.request.user.is_superuser

class RegistrationCodeList(UserPassesTestMixin, generic.ListView):
    model = RegistrationCode
    permission_denied_message = _('This page is only available to site admins')
    order_by = ['-expiry_date']
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context.get('is_paginated', False):
            return context
        current_page = context.get('page_obj').number
        context["previous_codes_count"] = self.paginate_by * (current_page - 1)
        return context

    def test_func(self):
        return self.request.user.is_superuser

class RegistrationCodeDelete(UserPassesTestMixin, generic.DeleteView):
    model = RegistrationCode
    permission_denied_message = _('This page is only available to site admins')
    success_url = reverse_lazy('code-list')

    def test_func(self):
        return self.request.user.is_superuser


from exchangeblog.models import BlogPost
from exchangeguide.models import GuidePost

def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name, {'latest_posts': BlogPost.objects.all()[:3], 'guide_teaser': GuidePost.objects.all()[:3]}, status=404)
    return response
