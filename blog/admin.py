from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date", "author")
    list_filter = ("author", "date", "tags")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")
    search_fields = ("first_name", "last_name", "email_address")

class TagAdmin(admin.ModelAdmin):
    list_display = ("caption", "slug")
    prepopulated_fields = {"slug": ("caption",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "user_email", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)