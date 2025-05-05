from django.contrib import admin
from .models import Category, Dish, SocialNetwork


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'is_visible', 'sort')
    list_display_links = ('id', 'name')
    list_editable = ('is_visible', 'sort')


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'link')

admin.site.register(Dish)