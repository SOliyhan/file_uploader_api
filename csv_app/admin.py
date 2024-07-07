from django.contrib import admin
from .models import Game


# Register your models here.


# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age', 'city', 'country')
#     search_fields = ('name', 'age', 'city')

admin.site.register(Game)