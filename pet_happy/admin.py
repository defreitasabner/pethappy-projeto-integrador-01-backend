from django.contrib import admin

from pet_happy.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, ClienteAdmin)
