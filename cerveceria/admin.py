from django.contrib import admin
from cerveceria.models import Cerveza, Distribuidor

# Register your models here.

class CervezaAdmin(admin.ModelAdmin):
    list_display = ("marca", "precio", "tamaño", "stock", "variedad")
    search_fields = ("marca", "precio")
    ordering = ("precio", "tamaño")
    list_filter = ("stock", "tamaño")

admin.site.register(Cerveza, CervezaAdmin)
admin.site.register(Distribuidor)
admin.site.site_header = "Administración de la cerveceria"