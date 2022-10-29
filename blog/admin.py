from django.contrib import admin
from .models import *

#admin.site.register(Post)
admin.site.register(Tag)


#Customize Admin to display more fields for Post Model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_approved', 'created')
