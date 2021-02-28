from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class RegistrationCode(models.Model):
    """A model for creating Registration Codes required for signup"""
    code = models.CharField(verbose_name=_("Registration Code"), max_length=7, unique=True, help_text=_('The registration code will be created automatically, so this field is disabled.'))
    has_blogauthor_permission = models.BooleanField(default=True, null=False, help_text=_('Specify wether the user using this code will be able to add blog posts.'))
    has_guidepost_permission = models.BooleanField(default=False, null=False, help_text=_('Specify wether the user using this code will be able to add guide posts.'))
    has_countryguide_permission = models.BooleanField(default=False, null=False, help_text=_('Specify wether the user using this code will be able to add a country guide about their country.'))
    expiry_date = models.DateField(default=datetime.now() + timedelta(days=30),help_text=_('The date upon which this code will be invalid, is automatically populated, but you can adjust it if you want.'))
    used_by = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-expiry_date']

    def check_if_valid(self):
        if self.expiry_date < datetime.now().date() or not self.used_by is None:
            return False
        else:
            return True
            
    def code_exists_and_valid(self):
        if RegistrationCode.objects.filter(code=self.code) and self.check_if_valid():
            return True
        else:
            return False

    @property
    def is_past_due(self):
        return self.expiry_date < datetime.today().date()

    def __str__(self):
            return self.code