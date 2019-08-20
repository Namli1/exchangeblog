from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class BlogPost(models.Model):
    """A model representing the blog posts for the Exchange-Blog"""
    title = models.CharField(help_text=_("Please enter the title of the Blog Post."), max_length=50)
    date_of_creation = models.DateField(help_text=_("Enter date of creation of post."), auto_now=False, auto_now_add=False)
    author = models.ForeignKey("BlogAuthor", on_delete=models.CASCADE)
    blogcontent = models.TextField(help_text=_("Please enter the text you want to publish."))

    class Meta:
        verbose_name_plural = ('blog posts')
        ordering = ['-date_of_creation']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class BlogPostImage(models.Model):
    property = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image_text = models.CharField(help_text=_("Please enter a short description of the picture."), max_length=150)
    image = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)

class BlogAuthor(models.Model):
    name = models.CharField(help_text=_("Please enter the name of the author."), max_length=20)
    bio = models.TextField(help_text=_("Please enter a short description of yourself."))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk}) 

    
