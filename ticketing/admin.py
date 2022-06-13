from django.contrib import admin
from ticketing.models import Ticheting , Category
class TichetingAdmin(admin.ModelAdmin):
    list_display = ['user' , 'title' , 'type' , 'description']


admin.site.register(Ticheting , TichetingAdmin)