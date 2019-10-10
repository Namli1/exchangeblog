from django import forms
from django.forms import ModelForm
from exchangeblog.models import BlogPost
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogPostCreate(CreateView):
    model = BlogPost
    success_url = reverse_lazy('post-list')