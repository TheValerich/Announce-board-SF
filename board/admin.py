from django.contrib import admin
from .models import (
    Post, Comment, Category, Author
)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('post', 'content', 'author')
    list_display_links = ('post', 'content', 'author')
    search_fields = ('post', 'content', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_activated')


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Author, AuthorAdmin)
