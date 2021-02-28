from django.shortcuts import render, get_object_or_404
from django import forms
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
from django.utils.translation import ugettext_lazy as _
from django.db import transaction
from django.urls import reverse_lazy
from exchangeguide.filters import CountryGuidePostFilter
from django_filters.views import FilterView
from exchangeblog.models import BlogAuthor, BlogPost
from django.db.models import F 
from .forms import CountryGuidePostForm, SlideShowImageForm, SlideShowImagesFormSet

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
            if GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).order_by('main_guide_post_number')[0:1]:
                context["next_post"] = GuidePost.objects.filter(main_guide_post_number__gt=self.get_object().main_guide_post_number).order_by('main_guide_post_number')[0:1]
            else:
                context['country_post'] = CountryGuidePost.objects.all().order_by('?')[0:2]
        except:
            context['country_post'] = CountryGuidePost.objects.all().order_by('?')[0:2]
        
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

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title, stopwords=['a', 'an', 'the', 'to', 'and', 'for'])
<<<<<<< HEAD
        form.instance.author = get_object_or_404(BlogAuthor, user=self.request.user)
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if CountryGuidePost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() + BlogPost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() >= max_posts:
=======
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if CountryGuidePost.objects.filter(author=form.instance.author).count() + BlogPost.objects.filter(author=form.instance.author).count() >= max_posts:
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
            raise PermissionDenied(_("You are not allowed to write more than {} posts").format(max_posts))
        return super().form_valid(form)

    def test_func(self):
<<<<<<< HEAD
        try:
            if not BlogAuthor.objects.filter(user=self.request.user).exists():
                raise PermissionDenied(_("You have to appy as a blog author before you can create any posts."))
        except:
            raise PermissionDenied(_("You have to apply for a user account to get the permission to add any posts."))
=======
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if CountryGuidePost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() + BlogPost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() >= max_posts:
            raise PermissionDenied(_("You are not allowed to write more than {} posts, sorry.").format(max_posts))
        return True

<<<<<<< HEAD
class GuidePostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = GuidePost
    fields = ['title', 'short_description', 'guide_content', 'thumbnail_picture',]
    permission_required = 'exchangeguide.add_guidepost'
    permission_denied_message = 'Permission denied. Please make sure you have permission to create and update a guide post.'

    def test_func(self):
        try:
            if not BlogAuthor.objects.filter(user=self.request.user).exists():
                raise PermissionDenied(_("You have to create a blog author profile before you can create or update any posts."))
        except:
            raise PermissionDenied(_("You have to apply for a user account to get the permission to add any posts."))
        obj = self.get_object()
        return obj.author == BlogAuthor.objects.get(user=self.request.user)
=======
class GuidePostUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = GuidePost
    fields = ['title', 'short_description', 'guide_content', 'thumbnail_picture',]
    permission_required = 'exchangeguide.change_guidepost'
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43

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
<<<<<<< HEAD
        if self.request.user.is_authenticated:
            try:
                post = self.get_object()
                if post.author == BlogAuthor.objects.get(user=self.request.user):
                    context["is_author"] = True
            except:
                pass
=======
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
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

<<<<<<< HEAD
class CountryGuidePostCreate(LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin, generic.CreateView):
    model = CountryGuidePost
    fields = ['guide_language', 'country', 'country_guide_content', 'spoken_language', 'population', 'capital_city', 'currency']
    permission_required = 'exchangeguide.add_countryguidepost'
    permission_denied_message = _("It seems like you don't have the permission to add a country guide post. Ask the admin via Instagram if you can get the permission to add a country guide post.")
=======
class CountryGuidePostCreate(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = CountryGuidePost
    fields = ['guide_language', 'country', 'country_guide_content', 'spoken_language', 'population', 'capital_city', 'currency']
    permission_required = 'exchangeguide.add_countryguidepost'
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
    success_url = reverse_lazy('countryguide-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = SlideShowImagesFormSet(self.request.POST, self.request.FILES)
        else:
            context["formset"] = SlideShowImagesFormSet()
        return context

    def test_func(self):
<<<<<<< HEAD
        if not BlogAuthor.objects.filter(user=self.request.user).exists():
            raise PermissionDenied(_("You have to create a blog author profile before you can create any posts."))
=======
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if CountryGuidePost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() + BlogPost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() >= max_posts:
            raise PermissionDenied(_("You are not allowed to write more than {} posts, sorry.").format(max_posts))
        return True
     
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
        if CountryGuidePost.objects.filter(author=form.instance.author).count() + BlogPost.objects.filter(author=form.instance.author).count() >= max_posts:
            raise PermissionDenied(_("You are not allowed to write more than {} posts").format(max_posts))
        return super().form_valid(form)

class CountryGuidePostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = CountryGuidePost
    fields = ['guide_language', 'country', 'country_guide_content', 'spoken_language', 'population', 'capital_city', 'currency']
    permission_required = 'exchangeguide.add_countryguidepost'

    def test_func(self):
<<<<<<< HEAD
        if not BlogAuthor.objects.filter(user=self.request.user).exists():
            raise PermissionDenied(_("You have to create a blog author profile before you can create or update any posts."))
=======
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
        obj = self.get_object()
        return obj.author == BlogAuthor.objects.get(user=self.request.user)

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
        formset = context["formset"]
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

class CountryGuidePostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = CountryGuidePost
    permission_required = 'exchangeguide.add_countryguidepost'
    success_url = reverse_lazy('blog')

    def test_func(self):
<<<<<<< HEAD
        if not BlogAuthor.objects.filter(user=self.request.user).exists():
            raise PermissionDenied(_("You have to create a blog author profile before you can create any posts which you might then delete."))
=======
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
        obj = self.get_object()
        return obj.author == BlogAuthor.objects.get(user=self.request.user)
