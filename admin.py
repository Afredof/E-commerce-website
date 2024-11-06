from django.contrib import admin
from . models import reg_table
from . models import item_table
from . models import cart_table,Pay_table
# Register your models here.
admin.site.register(reg_table)
admin.site.register(item_table)
admin.site.register(cart_table)
admin.site.register(Pay_table)