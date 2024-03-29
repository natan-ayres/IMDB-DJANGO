from django.contrib import admin
from app.models import Filmes

@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'desc', 'data', 'nota_media',
    ordering = '-id',
    search_fields = 'id', 'nome', 'data',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'nome', 'nota_media',
