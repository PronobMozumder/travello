from django.contrib import admin
from. models import destination


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'des', 'price', 'offer')
    list_filter = ("offer",)
    search_fields = ['name', 'price']

    
admin.site.register(destination, PostAdmin)