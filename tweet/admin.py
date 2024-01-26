from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import TweeterUser
from .models import Tweet, Comment


@admin.register(TweeterUser)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "first_name", "last_name", "email"),
            },
        ),
    )


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['text', 'last_update']
    list_per_page = 15
    search_fields = ['text']
    list_display_links = ['text']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'commented_time', 'id']

