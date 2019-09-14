from django.contrib import admin
from .models import Hall, Table, Order


# Register your models here.

admin.site.register(Hall)
admin.site.register(Table)
admin.site.register(Order)