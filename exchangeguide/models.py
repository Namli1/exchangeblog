from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from uuslug import slugify

# Create your models here.

class GuidePost(models.Model):
    title = models.CharField(_("Please enter the title of the Post"), max_length=50)
    slug = models.SlugField(_("Slug consisting of title of guide post."), unique=True, null=False, default="guidePost")
<<<<<<< HEAD
    author = models.ForeignKey("exchangeblog.BlogAuthor", on_delete=models.SET_NULL, null=True)
=======
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
    guide_content = RichTextUploadingField(config_name='blogpost-editor')
    short_description = models.TextField(_("Enter a short description about what this tutorial is about."), max_length=250)
    thumbnail_picture = ProcessedImageField(upload_to='guide_thumbnails/', processors=[ResizeToFill(500, 300)], options={'quality': 80}, max_length=100)
    main_guide_post_number = models.IntegerField(help_text=_("If post is part of the main step by step guide, enter its number in the order here."), unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("guide-detail", kwargs={"slug": self.slug})


class CountryGuidePost(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('DE', 'Deutsch'),
        ('IT', 'Italiano'),
        ('FR', 'Français'),
    ]
    guide_language = models.CharField(help_text=_('Please select the language you will use for the post.'), max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    COUNTRY_CHOICES = [
        ('CH', _('🇨🇳China')),
        ('US', _('🇺🇸USA')),
        ('UK', _('🇬🇧United Kingdom')),
        ('DE', _('🇩🇪Germany')),
        ('IT', _('🇮🇹Italy')),
        ('FR', _('🇫🇷France')),
        ('TH', _('🇹🇭Thailand')),
    ]
    country = models.CharField(max_length=2, help_text=_("Select the country you want to present."), choices=COUNTRY_CHOICES, default='CH')
    slug = models.SlugField(_("Slug consisting of country"), unique=True, null=False, default="countryguide")
<<<<<<< HEAD
    author = models.ForeignKey("exchangeblog.BlogAuthor", on_delete=models.SET_NULL, null=True)
=======
    author = models.ForeignKey("exchangeblog.BlogAuthor", on_delete=models.CASCADE)
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
    last_updated = models.DateField(help_text=_("Date guide was last updated."), auto_now=True)
    spoken_language = models.CharField(help_text=_("Enter the languages spoken in this country."), max_length=50)
    population = models.CharField(help_text=_("Enter the population of this country."), max_length=15)
    capital_city = models.CharField(help_text=_("Enter the capital city of this country."), max_length=20)
    currency = models.CharField(help_text=_("Enter what currency (money) is being used in this country."), max_length=20)
    short_description = models.CharField(help_text=_("Enter a short description about what makes this country special."), max_length=55, default=_("Check out this amazing country"))
    country_guide_content = RichTextUploadingField(help_text=_("Please select the Country Guide Template from the template button (Third symbol at top left)."), verbose_name="Main content", config_name="blogpost-editor")

    def __str__(self):
        return self.country

    def get_absolute_url(self):
        return reverse("countryguide-detail", kwargs={"slug": self.slug})


def get_image_filename(instance, filename):
    country = slugify(get_object_or_404(CountryGuidePost, country=instance.country).country)
    return "country_guide/slideshow/%s/%s" % (country, filename)

class SlideShowImages(models.Model):
    country = models.ForeignKey(CountryGuidePost, default=None, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to=get_image_filename, processors=[ResizeToFill(1000, 700)], options={'quality': 90}, max_length=100)
    image_description = models.CharField(help_text=_("Briefly describe what can be seen in picture."), max_length=50)

    def __str__(self):
        return "%s_%s" % (self.country, self.image)