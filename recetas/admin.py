from django.contrib import admin
from .models import TiposIngedientes, Ingrediente, Receta 

# Register your models here.
admin.site.register(TiposIngedientes)
admin.site.register(Ingrediente)
admin.site.register(Receta)