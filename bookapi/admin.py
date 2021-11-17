from django.contrib import admin
from bookapi.models import Book


# Register your models here.

class Books(admin.ModelAdmin):
    
    list_display = ('id','nome','descricao','nota')
    list_display_links = ('id','nome','descricao','nota')
    search_fields = ('nome','nota',)

admin.site.register(Book,Books)