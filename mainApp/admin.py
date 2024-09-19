from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class XaridorAdminClass(admin.ModelAdmin):
    model = Xaridor
    list_display = ['ism', 'familya', 'manzil', 'tel_1', 'tel_2']
    list_filter = ['ism', 'tel_1']


class SotuvAdminClass(admin.ModelAdmin):
    model = Sotuv
    list_display = ['meva_turi', 'bog', 'quti_turi', 'quti_soni','quti_ogirligi', 'tara', 'otish', 'narxi', 'xaridor', 'sana', 'formatted_foyda']
    list_filter = ['meva_turi', 'sana', 'bog', 'xaridor']
    list_editable = ['tara', 'otish', 'narxi',]


class XarajatlarAdminClass(admin.ModelAdmin):
    model = Xarajatlar
    list_display = ['umumiy_xarajat', 'sabab', 'sana']

admin.site.register(Xaridor, XaridorAdminClass)
admin.site.register(Sotuv, SotuvAdminClass)
admin.site.register(Xarajatlar, XarajatlarAdminClass)

admin.site.unregister(Group)
