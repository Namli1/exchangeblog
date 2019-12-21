from django.forms import ModelForm
from exchangeblog.models import BlogPost
from django.core.exceptions import ValidationError

""" class BlogPostCreateForm(ModelForm):
    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 4*1024*1024:
                raise ValidationError("Image file too large ( > 4mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")

    class Meta:
        model = BlogPost
        fields = ['title', 'language', 'country', 'blogcontent', 'thumbnail_picture'] """