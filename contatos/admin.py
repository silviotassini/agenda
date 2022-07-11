from django.contrib import admin

from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome', 'telefone', 'email','exibir')
    list_display_links = ('nome','sobrenome')
    list_filter = ('nome','sobrenome')
    search_fields = ('nome','sobrenome')
    list_editable = ('telefone','exibir')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)