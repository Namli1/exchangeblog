from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.exceptions import ValidationError
from uuslug import slugify

# Create your models here.

class BlogPost(models.Model):
    """A model representing the blog posts for the Exchange-Blog"""
    title = models.CharField(help_text=_("Please enter the title of the Blog Post."), max_length=50)
    date_of_creation = models.DateField(help_text=_("Enter date of creation of post."), auto_now_add=True)
    author = models.ForeignKey('BlogAuthor', on_delete=models.CASCADE)
    slug = models.SlugField(help_text="Enter a slug according to the title of the post",unique=True, null=False)
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
    blogcontent = RichTextUploadingField(config_name='blogpost-editor')
    thumbnail_picture = ProcessedImageField(upload_to='thumbnails/', processors=[ResizeToFill(300, 200)], options={'quality': 80}, max_length=100, null=True)

    class Meta:
        verbose_name_plural = ('blog posts')
        ordering = ['-date_of_creation']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug, "author": self.author.slug})


class BlogAuthor(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.SET_NULL, null=True)
    name = models.CharField(help_text=_("Please enter your author name (It will be displayed in articles you write)."), max_length=15, unique=True)
    slug = models.SlugField(null=False, unique=True)
    bio = models.TextField(help_text=_("Please enter a short description of yourself."))
    allowed_posts = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['name']
        permissions = (('can_edit_blogpost', 'Can create, update and delete a blogpost '),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={'slug': self.slug})

    
