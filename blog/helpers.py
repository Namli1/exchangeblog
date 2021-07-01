from exchangeblog.models import BlogAuthor, BlogPost
from exchangeguide.models import CountryGuidePost, GuidePost 
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _


def max_posts_test_func_create(self):
    try:
        if not BlogAuthor.objects.filter(user=self.request.user).exists():
            raise PermissionDenied(_("You have to appy as a blog author before you can create any posts."))
    except:
        raise PermissionDenied(_("You have to apply for a user account to get the permission to add any posts."))
    max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
    current_posts = CountryGuidePost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() + BlogPost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() + GuidePost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count()
    if current_posts >= max_posts:
        raise PermissionDenied(_("You are not allowed to write more than {} posts, sorry. Please contact the admin via Instagram to ask if you can write more.").format(max_posts))
    return True

def is_author_test_func(self):
    try:
        if not BlogAuthor.objects.filter(user=self.request.user).exists():
            raise PermissionDenied(_("You have to create a blog author profile before you can create or update any posts."))
    except:
        raise PermissionDenied(_("You have to apply for a user account to get the permission to add any posts."))
    obj = self.get_object()
    return obj.author == BlogAuthor.objects.get(user=self.request.user)