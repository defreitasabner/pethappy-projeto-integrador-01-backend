from django.contrib import admin

from pessoas.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa')
    list_display_links = ('id', 'pessoa')
    search_fields = ('pessoa',)
    list_per_page = 20

admin.site.register(Cliente, ClienteAdmin)
