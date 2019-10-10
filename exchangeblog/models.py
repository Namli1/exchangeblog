from django.db import models
from django import forms
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):
    """A model representing the blog posts for the Exchange-Blog"""
    title = models.CharField(help_text=_("Please enter the title of the Blog Post."), max_length=50)
    date_of_creation = models.DateField(help_text=_("Enter date of creation of post."), default=timezone.now)
    author = models.ForeignKey("BlogAuthor", on_delete=models.CASCADE)
    content = HTMLField('TextField')

    class Meta:
        verbose_name_plural = ('blog posts')
        ordering = ['-date_of_creation']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class BlogAuthor(models.Model):
    name = models.CharField(help_text=_("Please enter the name of the author."), max_length=20)
    bio = models.TextField(help_text=_("Please enter a short description of yourself."))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk}) 

