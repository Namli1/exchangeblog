from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CountryGuidePost, SlideShowImages

class CountryGuidePostForm(forms.ModelForm):
    class Meta:
        model = CountryGuidePost
        fields = ['guide_language', 'country', 'country_guide_content', 'short_description', 'spoken_language', 'population', 'capital_city', 'currency']


class SlideShowImageForm(forms.ModelForm):
    class Meta:
        model = SlideShowImages
        fields = ('image', 'image_description',)


SlideShowImagesFormSet = inlineformset_factory(CountryGuidePost, SlideShowImages, form=SlideShowImageForm, extra=1, max_num=10, can_delete=True)