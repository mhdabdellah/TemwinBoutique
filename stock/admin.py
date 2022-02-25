from django.contrib import admin
from .models import *


# Register your models here.


admin.site.register(Stock)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Entrer)
admin.site.register(Sortir)

admin.site.register(Facture)

