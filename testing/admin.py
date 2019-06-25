from django.contrib import admin
from .models import Beach, BeachNameID

# Register your models here.
admin.site.register(BeachNameID)
admin.site.register(Beach)