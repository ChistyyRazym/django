from django.contrib import admin

# Register your models here.
from .models import test_1

class test_1Admin(admin.ModelAdmin):
    list_display = ('id','ip','date','status_code','method', 'response_size','url')
    list_display_links = ('id','ip')
    search_fields = ('ip','status_code','date','url')
admin.site.register(test_1, test_1Admin)