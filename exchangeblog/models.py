from django.db import models
from django.urls import reverse
import random, datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field
from multiselectfield import MultiSelectField
from blog.general import COUNTRY_CHOICES, LANGUAGE_CHOICES

# Create your models here.

class BlogPost(models.Model):
    """A model representing the blog posts for the Exchange-Blog"""
    title = models.CharField(help_text=_("Please enter the title of the Blog Post."), max_length=50)
    date_of_creation = models.DateField(help_text=_("Enter date of creation of post."), default=datetime.date.today)
    author = models.ForeignKey('BlogAuthor', on_delete=models.CASCADE)
    slug = models.SlugField(help_text=_("Enter a slug according to the title of the post"), unique=True, null=False)
    language = models.CharField(help_text=_('Please enter the language you will use for the post.'), max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    country = models.CharField(max_length=2, help_text=_("Select the exchange country."), choices=COUNTRY_CHOICES, default='CH')
    short_description = models.TextField(max_length=150, help_text=_("Enter a short description of what the blog post is about."))
    blogcontent = CKEditor5Field(config_name='blogpost-editor')
    thumbnail_picture = ProcessedImageField(upload_to='thumbnails/', processors=[ResizeToFill(300, 200)], options={'quality': 80}, max_length=100, null=True)

    class Meta:
        verbose_name_plural = ('blog posts')
        ordering = ['-date_of_creation']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug, "author": self.author.slug})

    def get_random_post_url(self):
        random_post = random.choice(self.objects.all())
        return reverse("post-detail", kwargs={"slug": random_post.slug, "author": random_post.author.slug})


class BlogAuthor(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.PROTECT, null=True)
    name = models.CharField(help_text=_("Please enter your author name (It will be displayed in articles you write)."), max_length=19, unique=True)
    social_media_link = models.URLField(help_text=_("Please paste the url of your social media page (optional)."), blank=True, null=True, max_length=300)
    slug = models.SlugField(null=False, unique=True)
    bio = models.TextField(help_text=_("Please enter a short description of yourself."), max_length=400)
    allowed_posts = models.PositiveSmallIntegerField(default=1)
    allowed_countries = MultiSelectField(choices=COUNTRY_CHOICES, blank=True, null=True, help_text=_('The countries this author can write about in a country guide post.'))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={'slug': self.slug})

    def get_allowed_countries_choices(self):
        countries = self.allowed_countries
        tempDict = dict(COUNTRY_CHOICES)
        choices = []
        for country in self.allowed_countries:
            if country in tempDict:
                country_tuple = (country, tempDict.get(country))
                choices.append(country_tuple)
        return choices
        