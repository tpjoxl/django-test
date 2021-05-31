from django.contrib import admin
from .models import Post, setting
# Register your models here.

class settingAdmin(admin.ModelAdmin):
    list_display=('id','topic')
    list_filter=('topic',)
    search_fields=('topic',)
    
admin.site.register(setting, settingAdmin)