from django.contrib import admin

# Register your models here.

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'type', 'head')
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Config)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Link)