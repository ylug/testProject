from django.contrib import admin
from goods.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    Продукты - отображение в админ-панели Jango.
    Фильтрует по автору и названию продукта.
    Поиск по названию продукта.
    '''
    list_display = ('pk', 'author', 'title', 'model', 'release_date')
    list_filter = ('author', 'title',)
    search_fields = ('title',)

