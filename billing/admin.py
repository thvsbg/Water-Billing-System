from django.contrib import admin
from .models import prevBill,waterCharge,tax,dummy

# Register your models here.

admin.site.register(prevBill)
admin.site.register(waterCharge)
admin.site.register(tax)
admin.site.register(dummy)

