from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Post

# Register your models here.
'''
admin.site.register(Category)
admin.site.register(Post)
'''

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Post)    
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'slug', 'summary', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'slug')
    summernote_fields = ('content', 'summary')
    list_per_page = 10
    
