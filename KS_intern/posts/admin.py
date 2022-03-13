from django.contrib import admin
from .models import kstest


class kstestAdmin(admin.ModelAdmin):
    list_display = ('ks_ID', 'ks_Name','ks_Time')


    
admin.site.register(kstest)  #註冊至Administration(管理員後台)


