from django.contrib import admin

from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome', 'email')
    list_display_links = ('nome','sobrenome')
    list_filter = ('nome','sobrenome')
    search_fields = ('nome','sobrenome')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)