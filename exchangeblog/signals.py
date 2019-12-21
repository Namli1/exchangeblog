from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from exchangeblog.models import BlogPost

@receiver(post_save, sender=BlogPost)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm("can_edit_blogpost", instance.user, instance)