from django import forms
from exchangeblog.models import BlogAuthor
from django.utils.translation import ugettext_lazy as _

class BlogAuthorCreateForm(forms.ModelForm):
    class Meta:
        model = BlogAuthor
        fields = ("name", "social_media_link", "bio")
        widgets = {
            "social_media_link": forms.TextInput(attrs={'novalidate': True,}),
        }
