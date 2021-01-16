import requests
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
try:
    from blog import development_settings as settings
except ImportError as e:
    from blog import settings

class SignUpWithCodeForm(UserCreationForm):
    registration_code = forms.CharField(label=_("Registration Code"), max_length=7, required=True, help_text=_("Please enter the registration code given to you to register your account. (You cannot sign up without a registration code. Contact us on Instagram to request a code.)"))
    recaptcha = forms.CharField(
        widget=forms.HiddenInput(),
        max_length=1024,
        required=False
    )

    def clean_registration_code(self):
        registration_code = self.cleaned_data['registration_code']
        if registration_code == '1':
            return True
        else:
            raise ValidationError(_("Invalid registration code. Please make sure you spelled it correctly. Otherwise contact the admin."), code='invalid')
        return False

    def clean(self):
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
            print(result)
            pass
        else:
            raise forms.ValidationError(_('We couldn\'t verify that you are not a robot. Please try again.'))

    class Meta:
        model = User
        fields = ('email', 'recaptcha',)