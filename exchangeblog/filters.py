import django_filters
import datetime
from django import forms

from .models import BlogPost, BlogAuthor

current_year = datetime.datetime.now().year

class BlogPostFilter(django_filters.FilterSet):
    empty_value = 'EMPTY'
    YEAR_CHOICES = (
    (2019, 2019),
    (2020, 2020))

    def filter(self, qs, value):
        if value != self.empty_value:
            return super().filter(qs, value)

        qs = self.get_method(qs)(**{'%s__%s' % (self.field_name, self.lookup_expr): ""})
        return qs.distinct() if self.distinct else qs

    author = django_filters.ModelMultipleChoiceFilter(queryset=BlogAuthor.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'js-filter-multiple', 'style': 'width: 100%;', 'id': 'author', 'aria-describedby': 'authorfilter-help'}))
    language = django_filters.MultipleChoiceFilter(choices=BlogPost.LANGUAGE_CHOICES, widget=forms.SelectMultiple(attrs={'class': 'js-filter-multiple', 'style': 'width: 100%;','id': 'language', 'aria-describedby': 'languagefilter-help', 'multiple': 'multiple'}))
    country = django_filters.MultipleChoiceFilter(choices=BlogPost.COUNTRY_CHOICES, widget=forms.SelectMultiple(attrs={'class': 'js-filter-multiple', 'style': 'width: 100%;', 'id': 'country', 'aria-describedby': 'countryfilter-help'}))
    date_of_creation = django_filters.ChoiceFilter(choices=YEAR_CHOICES, lookup_expr='year', widget=forms.Select(attrs={'class': 'custom-select custom-select-sm', 'aria-describedby': 'datefilter-help'}))
    
    class Meta:
        model = BlogPost
        fields = ['author', 'language', 'country', 'date_of_creation']