from django.contrib import admin
from exchangeguide.models import GuidePost, CountryGuidePost, SlideShowImages

# Register your models here.
admin.site.register(SlideShowImages)
admin.site.register(GuidePost)

class SlideShowImagesInline(admin.TabularInline):
    model = SlideShowImages

@admin.register(CountryGuidePost)
class CountryGuidePostAdmin(admin.ModelAdmin):
    list_display = ('country',)
    inlines = [SlideShowImagesInline]