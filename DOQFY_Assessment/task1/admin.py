from django.contrib import admin
from .models import UrlModel

class UrlModelAdmin(admin.ModelAdmin):
    list_display = ('id','url', 'short_url') 
    search_fields = ('url', 'short_url') 
    fields = ('short_url',)
    readonly_fields = ('url',)

# Register the model with the custom admin class
admin.site.register(UrlModel, UrlModelAdmin)
