from django.contrib import admin
from blog.models import Author, Post, Tags, Comment
from django.utils.safestring import mark_safe

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "show_photo")
    list_display_links = ["full_name"]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' style='max-height:100px;'>")
    show_photo.short_description = 'Author'

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    list_display_links = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_display_links = ['title',] 
    list_filter = ['created_at',]
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email') 
    list_display_links = ('name', 'email')
    list_filter = ['created_at',] 
