from django.contrib import admin
from .models import Event 
from .models import Apply

# Register your models here.

admin.site.register(Event)
admin.site.register(Apply)