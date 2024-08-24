from django.contrib import admin
from .models import SnippetModel

class SnippetModelAdmin(admin.ModelAdmin):
    list_display = ('id','text', 'secret_key', 'shareable_url')
    search_fields = ('test',) 
    fields = ('text',)
    readonly_fields = ('secret_key', 'shareable_url')

# Register the model with the custom admin class
admin.site.register(SnippetModel, SnippetModelAdmin)


# Register your models here.
