from django.contrib import admin
from .models import Feed

# Register your models here.
@admin.register(Feed)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    list_display_links = ['id', 'title']