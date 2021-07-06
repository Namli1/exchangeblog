from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CountryGuidePost, SlideShowImages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from exchangeblog.models import BlogAuthor

class SlideShowImageForm(forms.ModelForm):
    class Meta:
        model = SlideShowImages
        fields = ('image', 'image_description',)

class CountryGuidePostCreateForm(forms.ModelForm):
    class Meta:
        model = CountryGuidePost
        fields = ['guide_language', 'country', 'spoken_language', 'population', 'capital_city', 'currency', 'short_description', 'country_guide_content',]

    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user')
         #set empty initial for short_description
         initial = kwargs.get('initial', {})
         initial['short_description'] = ''
         kwargs['initial'] = initial
         author = BlogAuthor.objects.filter(user=self.user).first()
         super(CountryGuidePostCreateForm, self).__init__(*args, **kwargs)
         self.fields['country'].choices = author.get_allowed_countries_choices()


SlideShowImagesFormSet = inlineformset_factory(CountryGuidePost, SlideShowImages, form=SlideShowImageForm, extra=1, max_num=10, can_delete=True)