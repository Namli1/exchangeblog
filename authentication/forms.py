import requests
import string
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError
from django.conf import settings
from django.utils.crypto import get_random_string

from authentication.models import RegistrationCode

class SignUpWithCodeForm(UserCreationForm):
    registration_code = forms.CharField(label=_("Registration Code"), max_length=7, required=True, help_text=_("Please enter the registration code given to you to register your account. (You cannot sign up without a registration code. Contact us on Instagram to request a code.)"))
    recaptcha = forms.CharField(
        widget=forms.HiddenInput(),
        max_length=1024,
        required=False
    )

    def clean_registration_code(self):
        registration_code = self.cleaned_data['registration_code']
        if RegistrationCode.objects.filter(code=registration_code).exists():
            if RegistrationCode.objects.filter(code=registration_code).first().check_if_valid():
                    return registration_code
            else:
                raise ValidationError(_("Invalid registration code. This code has either been used before or it has expired. Please make sure you spelled it correctly. If it's not working, contact the admin via Instagram."), code='invalid')
        else:
            raise ValidationError(_("Invalid registration code. This code does not exist. Please make sure you've spelled it correctly. If it's still not working, contact the admin via Instagram."), code='invalid')
        return False

    def clean(self):
        #ReCaptcha implementation
        cleaned_data = super(SignUpWithCodeForm, self).clean()
        recaptcha_token = cleaned_data.get('recaptcha')
        recaptcha_data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_token,
        }
        response = requests.post(
                'https://www.recaptcha.net/recaptcha/api/siteverify',
                data = recaptcha_data
            )
        result = response.json()
        if result.get('success') and result.get('score') > 0.8 and result['action'] == 'submit':
            # client is human
            pass
        else:
            raise forms.ValidationError(_('We couldn\'t verify that you are not a robot. Please try again.'))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'registration_code', 'recaptcha',)

    def __init__(self, *args, **kwargs):
        super(SignUpWithCodeForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

class PasswordResetFormWithReCaptcha(PasswordResetForm):
    recaptcha = forms.CharField(
        widget=forms.HiddenInput(),
        max_length=1024,
        required=False
    )

    def clean(self):
        cleaned_data = super(PasswordResetFormWithReCaptcha, self).clean()
        recaptcha_token = cleaned_data.get('recaptcha')
        recaptcha_data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_token,
        }
        response = requests.post(
                'https://www.recaptcha.net/recaptcha/api/siteverify',
                data = recaptcha_data
            )
        result = response.json()
        if result.get('success') and result.get('score') > 0.8 and result['action'] == 'submit':
            # client is human
            pass
        else:
            raise forms.ValidationError(_('We couldn\'t verify that you are not a robot. Please try again.'))

    class Meta:
        model = User
        fields = ('email', 'recaptcha',)

class RegistrationCodeForm(forms.ModelForm):
    code = forms.CharField(disabled=True, initial=get_random_string(length=7, allowed_chars=string.ascii_uppercase + string.digits), label=_('Registration Code'), help_text=_('The registration code will be created automatically, so this field is disabled.'))

    def clean_code(self):
        code = self.cleaned_data['code']
        if RegistrationCode.objects.filter(code=code).exists():
            while RegistrationCode.objects.filter(code=code).exists():
                new_random_code = get_random_string(length=7)
                code = new_random_code
                self.cleaned_data['code'] = new_random_code
        return code

    class Meta:
        model = RegistrationCode
        fields = ('code', 'has_blogauthor_permission', 'has_guidepost_permission', 'has_countryguide_permission', 'allowed_countries', 'max_post_count', 'expiry_date',)
