from django.contrib import admin
from .models import *

admin.site.register(Group)


@admin.register(MenuItem)
class ImportantV(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'section', )
    list_display_links = ('name', )
    list_filter = ('section', )