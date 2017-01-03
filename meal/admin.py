from django.contrib import admin
from .models import Meal, ItemMeal, Plate, Allergy

# Register your models here.

admin.site.register(Meal)
admin.site.register(ItemMeal)
admin.site.register(Allergy)
admin.site.register(Plate)
