from django.contrib import admin
from .models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ('nome', )


class CarAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_lancamento', 'valor')
    search_fields = ('modelo',)

admin.site.register(Car, CarAdmin),
admin.site.register(Brand, BrandAdmin)