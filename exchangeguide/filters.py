import django_filters
import datetime
from django import forms

from .models import CountryGuidePost

class CountryGuidePostFilter(django_filters.FilterSet):
    empty_value = 'EMPTY'

    def filter(self, qs, value):
        if value != self.empty_value:
            return super().filter(qs, value)

        qs = self.get_method(qs)(**{'%s__%s' % (self.field_name, self.lookup_expr): ""})
        return qs.distinct() if self.distinct else qs

    country = django_filters.MultipleChoiceFilter(choices=CountryGuidePost.COUNTRY_CHOICES, widget=forms.SelectMultiple(attrs={'class': 'js-filter-multiple', 'style': 'width: 100%;', 'id': 'country', 'aria-describedby': 'countryfilter-help'}))

    class Meta:
        model = CountryGuidePost
        fields = ["country"]