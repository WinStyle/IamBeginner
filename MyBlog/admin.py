from django.contrib import admin
from MyBlog.models import *

# Register your models here.
admin.site.register(ArticleTarget)
#admin.site.register(Article)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/media/js/tiny_mce/tiny_mce.js',
            '/media/js/textareas.js',
        )
admin.site.register(Article, BlogAdmin)