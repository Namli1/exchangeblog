from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from blog.general import COUNTRY_CHOICES

class RegistrationCode(models.Model):
    """A model for creating Registration Codes required for signup"""
    code = models.CharField(verbose_name=_("Registration Code"), max_length=7, unique=True, help_text=_('The registration code will be created automatically, so this field is disabled.'))
    has_blogauthor_permission = models.BooleanField(verbose_name=_("Has blogauthor permission"), default=True, null=False, help_text=_('Specify wether the user using this code will be able to add blog posts.'))
    has_guidepost_permission = models.BooleanField(verbose_name=_("Has guidepost permission"), default=False, null=False, help_text=_('Specify wether the user using this code will be able to add guide posts.'))
    has_countryguide_permission = models.BooleanField(verbose_name=_("Has countryguidepost permission"), default=False, null=False, help_text=_('Specify wether the user using this code will be able to add a country guide about their country.'))
    allowed_countries = MultiSelectField(verbose_name=_("Allowed countries"), choices=COUNTRY_CHOICES, blank=True, null=True, help_text=_('The allowed countries the author can write about when creating a country guide post.'))
    expiry_date = models.DateField(verbose_name=_("Expiry date"), default=datetime.now() + timedelta(days=30),help_text=_('The date upon which this code will be invalid, is automatically populated, but you can adjust it if you want.'))
    used_by = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Used by"), )

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

    def check_if_used_by_this_user(self, user):
        if self.expiry_date > datetime.now().date() and (self.used_by == user):
            return True
        else:
            return False

    @property
    def is_past_due(self):
        return self.expiry_date < datetime.today().date()

    def __str__(self):
            return self.code
