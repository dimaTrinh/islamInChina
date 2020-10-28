from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Person)
admin.site.register(Place)
admin.site.register(Work)
admin.site.register(Page)
