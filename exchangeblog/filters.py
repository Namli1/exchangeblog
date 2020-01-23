import django_filters
import datetime
from django import forms

from .models import BlogPost, BlogAuthor

current_year = datetime.datetime.now().year

class BlogPostFilter(django_filters.FilterSet):
    YEAR_CHOICES = (
    (2019, 2019),
    (2020, 2020)
    )
    author = django_filters.ModelChoiceFilter(queryset=BlogAuthor.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm custom-select custom-select-sm', 'aria-describedby': 'authorfilter-help'}))
    language = django_filters.ChoiceFilter(choices=BlogPost.LANGUAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm custom-select custom-select-sm', 'aria-describedby': 'languagefilter-help'}))
    country = django_filters.ChoiceFilter(choices=BlogPost.COUNTRY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm custom-select custom-select-sm', 'id': 'country', 'aria-describedby': 'countryfilter-help'}))
    date_of_creation = django_filters.ChoiceFilter(choices=YEAR_CHOICES, lookup_expr='year', widget=forms.Select(attrs={'class': 'custom-select custom-select-sm', 'aria-describedby': 'datefilter-help'}))
    
    class Meta:
        model = BlogPost
        fields = ['language', 'country',]