from django import forms
from exchangeblog.models import BlogAuthor
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError

from authentication.models import RegistrationCode

class BlogAuthorCreateForm(forms.ModelForm):
    registration_code = forms.CharField(label=_("Registration Code"), max_length=7, required=True, help_text=_("Please enter the registration code given to you to register your account (The one you already used on sign-up)."))

    def clean_registration_code(self):
        registration_code = self.cleaned_data['registration_code']
        if RegistrationCode.objects.filter(code=registration_code).exists():
            if RegistrationCode.objects.filter(code=registration_code).first().check_if_used_by_this_user(user=self.user):
                    print("Passed test")
                    return registration_code
            else:
                print(self.user)
                raise ValidationError(_("Invalid registration code. This code has probably expired. Please make sure you spelled it correctly. If it's not working, contact the admin via Instagram."), code='invalid')
        else:
            raise ValidationError(_("Invalid registration code. This code does not exist. Please make sure you've spelled it correctly. If it's still not working, contact the admin via Instagram."), code='invalid')
        return False

    class Meta:
        model = BlogAuthor
        fields = ("name", "social_media_link", "bio", 'registration_code')
        widgets = {
            "social_media_link": forms.TextInput(attrs={'novalidate': True,}),
        }

    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user')
         super(BlogAuthorCreateForm, self).__init__(*args, **kwargs)