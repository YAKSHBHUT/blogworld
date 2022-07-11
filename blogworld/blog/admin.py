
from django.contrib import admin
from .models import Categorie, Post
# Register your models here.


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'url', 'add_date')
    search_fields = ('title',)

    class Media:
        js = (
            'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'url')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5

    class Media:
        js = (
            'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Post, PostAdmin)
