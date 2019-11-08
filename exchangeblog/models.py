from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    """A model representing the blog posts for the Exchange-Blog"""
    title = models.CharField(help_text=_("Please enter the title of the Blog Post."), max_length=50)
    date_of_creation = models.DateField(help_text=_("Enter date of creation of post."), auto_now_add=True)
    author = models.ForeignKey("BlogAuthor", on_delete=models.CASCADE)
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('DE', 'Deutsch'),
        ('IT', 'Italiano'),
        ('FR', 'Français'),
    ]
    language = models.CharField(help_text=_('Please enter the language you will use for the post.'),max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    COUNTRY_CHOICES = [
        ('CH', '🇨🇳China'),
        ('US', '🇺🇸USA'),
        ('UK', '🇬🇧United Kingdom'),
        ('DE', '🇩🇪Germany'),
        ('IT', '🇮🇹Italy'),
        ('FR', '🇫🇷France'),
        ('TH', '🇹🇭Thailand'),
    ]
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='CH')
    blogcontent = tinymce_models.HTMLField()

    class Meta:
        verbose_name_plural = ('blog posts')
        ordering = ['-date_of_creation']
        permissions = (('can_create_post', 'Create a blog post'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class BlogAuthor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(help_text=_("Please enter your author name (It will be displayed in articles you write)."), max_length=20)
    bio = models.TextField(help_text=_("Please enter a short description of yourself."))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk}) 

    
