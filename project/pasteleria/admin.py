from django.contrib import admin
from .models import Cliente, Tortas, Pedido
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Tortas)
admin.site.register(Pedido)
