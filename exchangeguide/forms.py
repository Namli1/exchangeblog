from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CountryGuidePost, SlideShowImages
from exchangeblog.models import BlogAuthor

class SlideShowImageForm(forms.ModelForm):
    class Meta:
        model = SlideShowImages
        fields = ('image', 'image_description',)

class CountryGuidePostCreateForm(forms.ModelForm):
    class Meta:
        model = CountryGuidePost
        fields = ['guide_language', 'country', 'country_guide_content', 'spoken_language', 'population', 'capital_city', 'currency']

    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user')
         author = BlogAuthor.objects.filter(user=self.user).first()
         super(CountryGuidePostCreateForm, self).__init__(*args, **kwargs)
         self.fields['country'].choices = author.get_allowed_countries_choices()


SlideShowImagesFormSet = inlineformset_factory(CountryGuidePost, SlideShowImages, form=SlideShowImageForm, extra=1, max_num=10, can_delete=True)