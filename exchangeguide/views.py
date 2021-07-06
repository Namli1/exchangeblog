from django.shortcuts import render, get_object_or_404
from django import forms
from itertools import chain
import random
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from exchangeguide.models import CountryGuidePost, GuidePost, SlideShowImages
from exchangeblog.models import BlogAuthor, BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views import generic
from uuslug import slugify
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from django.urls import reverse_lazy
from exchangeguide.filters import CountryGuidePostFilter
from django_filters.views import FilterView
from exchangeblog.models import BlogAuthor, BlogPost
from django.db.models import F
from .forms import SlideShowImageForm, SlideShowImagesFormSet, CountryGuidePostCreateForm
from blog.helpers import max_posts_test_func_create, is_author_test_func
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your views here.

#GuidePost
class GuidePostDetailView(generic.DetailView):
    model = GuidePost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if (GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).order_by('main_guide_post_number')[0:1]):
        #     context["next_post"] = GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).order_by('main_guide_post_number')[0:1]
        # else:
        #     context['country_post'] = CountryGuidePost.objects.all().order_by('?')[0:2]

        try:
            #Pass the next two ordered posts if they exist
            if GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).count() >= 2:
                context["next_posts"] = GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).order_by('main_guide_post_number')[0:2]
            #If there are no two ordered posts, look if there is one ordered post and one unordered post
            elif GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).exists() and GuidePost.objects.filter(main_guide_post_number__isnull=True).exists():
                guide_post = GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).order_by('main_guide_post_number')[0:1]
                unordered_post = GuidePost.objects.filter(main_guide_post_number__isnull=True).order_by('?')[0:1]
                context["next_posts"] = list(chain(guide_post, unordered_post))
            #If there are no two posts, pass only the next one 
            elif GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).count() >= 1:
                context["next_posts"] = GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).order_by('main_guide_post_number')[0:1]
            else:
                context['country_post'] = CountryGuidePost.objects.all().order_by('?')[0:2]
        except:
             pass

        if CountryGuidePost.objects.all().count() > 0:
            context['country_post'] = CountryGuidePost.objects.all().order_by('?')[0:2]
        elif BlogPost.objects.all().count() >= 2:
            context['blog_post'] = BlogPost.objects.all().order_by('?')[0:2]
        elif BlogPost.objects.all().count() >= 1:
            print("hi there")
            context['blog_post'] = BlogPost.objects.all().order_by('?')[0:1]
        if self.request.user.is_authenticated:
            try:
                if BlogAuthor.objects.get(user=self.request.user):
                    context["is_author"] = BlogAuthor.objects.get(user=self.request.user).slug
            except:
                pass
        return context
    

class GuidePostListView(generic.ListView):
    model = GuidePost
    paginate_by = 15
    queryset = GuidePost.objects.all().order_by(F('main_guide_post_number').asc(nulls_last=True))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                if BlogAuthor.objects.get(user=self.request.user):
                    context["is_author"] = BlogAuthor.objects.get(user=self.request.user).slug
            except:
                pass
        return context
    

class GuidePostCreate(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = GuidePost
    fields = ['title', 'short_description', 'guide_content', 'thumbnail_picture',]
    permission_required = 'exchangeguide.add_guidepost'
    permission_denied_message = 'Permission denied. Please make sure you have permission to create a guide post.'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Create'))
        return form

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title, stopwords=['a', 'an', 'the', 'to', 'and', 'for'])
        form.instance.author = get_object_or_404(BlogAuthor, user=self.request.user)
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        print(CountryGuidePost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() + BlogPost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() >= max_posts)
        if CountryGuidePost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() + BlogPost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() >= max_posts:
            raise PermissionDenied(_("You are not allowed to write more than {} posts. Please contact the admin via Instagram to ask if you can write more.").format(max_posts))
        return super().form_valid(form)

    def test_func(self):
        return max_posts_test_func_create(self)

class GuidePostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = GuidePost
    fields = ['title', 'short_description', 'guide_content', 'thumbnail_picture',]
    permission_required = 'exchangeguide.add_guidepost'
    permission_denied_message = 'Permission denied. Please make sure you have permission to create and update a guide post.'

    def test_func(self):
        return is_author_test_func(self)

class GuidePostDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = GuidePost
    permission_required = 'exchangeguide.delete_guidepost'
    success_url = reverse_lazy('guide-list')


#CountryGuidePost
class CountryGuidePostDetailView(generic.DetailView):
    model = CountryGuidePost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Get 3 random objects from CountryGuidePost
        context["other_country_guides"] = CountryGuidePost.objects.order_by('?')[:2]
        current_author = self.get_object().author
        context['num_authors_posts'] = BlogPost.objects.filter(author=current_author).count()
        context['more_posts_from_author'] = BlogPost.objects.filter(author=current_author).exclude(slug=self.get_object().slug)[:2]
        context['more_posts_from_country'] = BlogPost.objects.filter(country=self.get_object().country)[:2]
        if self.request.user.is_authenticated:
            try:
                post = self.get_object()
                if post.author == BlogAuthor.objects.get(user=self.request.user):
                    context["is_author"] = True
            except:
                pass
        return context
    

class CountryGuideListView(FilterView):
    model = CountryGuidePost
    filterset_class = CountryGuidePostFilter
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.copy()
        if 'page' in query:
            del query['page']
        context['querystring'] = query.urlencode()
        context['country_guide_list'] = CountryGuidePostFilter(self.request.GET, queryset=self.get_queryset())
        if self.request.user.is_authenticated:
            try:
                if BlogAuthor.objects.get(user=self.request.user):
                    context["is_author"] = BlogAuthor.objects.get(user=self.request.user).slug
            except:
                pass
        return context

class CountryGuidePostCreate(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.CreateView):
    form_class = CountryGuidePostCreateForm
    # fields = ['guide_language', 'country', 'country_guide_content', 'spoken_language', 'population', 'capital_city', 'currency']
    template_name = 'exchangeguide/countryguidepost_form.html'
    permission_required = 'exchangeguide.add_countryguidepost'
    permission_denied_message = _("It seems like you don't have the permission to add a country guide post. Ask the admin via Instagram if you can get the permission to add a country guide post.")
    success_url = reverse_lazy('countryguide-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = SlideShowImagesFormSet(self.request.POST, self.request.FILES)
        else:
            context["formset"] = SlideShowImagesFormSet()
        return context
    
    def get_form_kwargs(self):
        kwargs = super(CountryGuidePostCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        try:
            allowed_countries = get_object_or_404(BlogAuthor, user=self.request.user).get_allowed_countries_choices()
            if not allowed_countries:
                return False
        except:
            return max_posts_test_func_create(self)
        return max_posts_test_func_create(self)
     
    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.author = get_object_or_404(BlogAuthor, user=self.request.user)
        form.instance.slug = slugify(form.instance.get_country_display().encode('ascii', 'ignore').decode('ascii'))
        formset = context["formset"]
        with transaction.atomic():
            self.object = form.save()

            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if CountryGuidePost.objects.filter(author=form.instance.author).count() + BlogPost.objects.filter(author=form.instance.author).count() >= max_posts + 1:
            raise PermissionDenied(_("You are not allowed to write more than {} posts. Please contact the admin via Instagram to ask if you can write more.").format(max_posts))
        return super().form_valid(form)

class CountryGuidePostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = CountryGuidePost
    fields = ['guide_language', 'country', 'country_guide_content', 'spoken_language', 'population', 'capital_city', 'currency']
    permission_required = 'exchangeguide.add_countryguidepost'

    def test_func(self):
        return is_author_test_func(self)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = SlideShowImagesFormSet(self.request.POST, self.request.FILES, instance=self.get_object())
            context["formset"].full_clean()
        else:
            context["formset"] = SlideShowImagesFormSet(instance=self.get_object())
        return context
     
    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.slug = slugify(form.instance.get_country_display().encode('ascii', 'ignore').decode('ascii'))
        formset = context["formset"]
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

class CountryGuidePostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = CountryGuidePost
    permission_required = 'exchangeguide.countryguidepost_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return is_author_test_func(self)