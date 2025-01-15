from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Chicken, Egg

class ChickenAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'health_status')  # Show these fields in list view
    list_filter = ('health_status', 'breed')  # Add filters by health_status and breed
    search_fields = ('name',)  # Add a search bar for name
    
    fieldsets = (
        (None, {
            'fields': ('name', 'age', 'breed', 'health_status')
        }),
    )

class EggAdmin(admin.ModelAdmin):
    list_display = ('chicken', 'quantity', 'date_collected')  # Show chicken, quantity, and date_collected
    list_filter = ('chicken', 'date_collected')  # Add filters for chicken and date_collected

admin.site.register(Chicken, ChickenAdmin)
admin.site.register(Egg, EggAdmin)
