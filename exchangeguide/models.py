from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from uuslug import slugify
from blog.general import COUNTRY_CHOICES, LANGUAGE_CHOICES

# Create your models here.

class GuidePost(models.Model):
    title = models.CharField(verbose_name=_("Title"), help_text=_("Please enter the title of the Post"), max_length=70)
    slug = models.SlugField(help_text=_("Slug consisting of title of guide post."), unique=True, null=False, default="guidePost")
    author = models.ForeignKey("exchangeblog.BlogAuthor", verbose_name=_("Author"),  on_delete=models.SET_NULL, null=True)
    guide_content = CKEditor5Field(config_name='blogpost-editor', verbose_name=_("Guide content"), help_text=_("Here is the place to write the actual guide itself."))
    short_description = models.TextField(verbose_name=_("Short description"), help_text=_("Enter a short description about what this tutorial is about."), max_length=250)
    thumbnail_picture = ProcessedImageField(verbose_name=_("Thumbnail picture"), upload_to='guide_thumbnails/', processors=[ResizeToFill(500, 300)], options={'quality': 80}, max_length=100)
    main_guide_post_number = models.IntegerField(verbose_name=_("Main Guide Post Number"), help_text=_("If post is part of the main step by step guide, enter its number in the order here."), unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("guide-detail", kwargs={"slug": self.slug})


class CountryGuidePost(models.Model):
    guide_language = models.CharField(verbose_name=_("Guide language"), help_text=_('Please select the language you will use for the post.'), max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    country = models.CharField(verbose_name=_("Country"), max_length=2, help_text=_("Select the country you want to present."), choices=COUNTRY_CHOICES, default='CH', unique=True)
    slug = models.SlugField(verbose_name=_("Slug"), help_text=_("Slug consisting of country"), unique=True, null=False, default="countryguide")
    author = models.ForeignKey("exchangeblog.BlogAuthor", verbose_name=_("Author"), on_delete=models.SET_NULL, null=True)
    last_updated = models.DateField(verbose_name=_("Last updated"), help_text=_("Date guide was last updated."), auto_now=True)
    spoken_language = models.CharField(verbose_name=_("Spoken language"), help_text=_("Enter the languages spoken in this country."), max_length=50)
    population = models.CharField(verbose_name=_("Population"), help_text=_("Enter the population of this country."), max_length=15)
    capital_city = models.CharField(verbose_name=_("Capital city"), help_text=_("Enter the capital city of this country."), max_length=20)
    currency = models.CharField(verbose_name=_("Currency"), help_text=_("Enter what currency (money) is being used in this country."), max_length=20)
    short_description = models.CharField(verbose_name=_("Short description"), help_text=_("Enter a short description about what makes this country special."), max_length=55, default=_("Check out this amazing country"))
    country_guide_content = CKEditor5Field(help_text=_("Describe the most important things and aspects about the country (e.g. food, people, culture, school, ...)"), verbose_name="Main content", config_name='blogpost-editor',)

    def __str__(self):
        return self.country

    def get_absolute_url(self):
        return reverse("countryguide-detail", kwargs={"slug": self.slug})


def get_image_filename(instance, filename):
    country = slugify(get_object_or_404(CountryGuidePost, country=instance.country).country)
    return "country_guide/slideshow/%s/%s" % (country, filename)

class SlideShowImages(models.Model):
    country = models.ForeignKey(CountryGuidePost, default=None, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to=get_image_filename, processors=[ResizeToFill(1100, 700)], options={'quality': 60}, max_length=100)
    image_description = models.CharField(help_text=_("Briefly describe what can be seen in picture."), max_length=50)

    def __str__(self):
        return "%s_%s" % (self.country, self.image)