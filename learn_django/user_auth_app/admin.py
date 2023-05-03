from django.contrib import admin
from .models import Image

class imageadmin(admin.ModelAdmin):
    list_display = ["user","title","photo"]

admin.site.register(Image,imageadmin)
