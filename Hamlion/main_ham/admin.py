from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import For_man, Category, For_Women, Tovars, Corzina, Product


# Register your models here.

class For_ManAdmin(admin.ModelAdmin):
    list_display = ['id','name_tovar','about_the_tovar','get_image','size','color','price','double_table','image_tovar','articul_tovar','sostav_tovar','season','country']
    list_editable = ['name_tovar','about_the_tovar','size','color','articul_tovar','double_table','price','sostav_tovar','season','country']

    def get_image(self,obj):
        return f'<img src "media/{For_man.image_tovar}" '

class CorzinaAdmin(admin.ModelAdmin):
    list_display = ['id_clothes', 'accounte','count','price_for_tovars']
    list_editable = ['accounte','count','price_for_tovars']

class TovarsAdmin(admin.ModelAdmin):
    list_display = ['id_clothes', 'accounte', 'like']
    list_editable = ['accounte', 'like']

class For_WomenAdmin(admin.ModelAdmin):
    list_display = ['name_tovar','about_the_tovar','price','double_table','image_tovar','articul_tovar','sostav_tovar','season','country']
    list_editable = ['about_the_tovar','articul_tovar','double_table','price','sostav_tovar','season','country']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['persons','category']
    list_editable = ['category']





admin.site.register(For_man,For_ManAdmin)
admin.site.register(Tovars,TovarsAdmin)
admin.site.register(Corzina,CorzinaAdmin)
admin.site.register(Product)
admin.site.register(For_Women,For_WomenAdmin)
admin.site.register(Category,CategoryAdmin)
