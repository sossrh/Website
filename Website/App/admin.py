from django.contrib import admin
from .models import *

# Register your models here.

class ProductDetails(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class SandwichDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class SouthindianDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class PizzaDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class BurgerDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')    

class RollDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class FingerFoodDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class DessertDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class BeverageDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class SauceDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class SoupsDeatils(admin.ModelAdmin):
    list_display=('id','name', 'price', 'category','image', 'type')

class CategoryDetails(admin.ModelAdmin):
    list_display=('id','name',)

class ContactDetails(admin.ModelAdmin):
    list_display=('id','name', 'email', 'message',)

# class CartDetails(admin.ModelAdmin):
#     list_display=('id','user', 'items',)
    
# class CartItemsDisplay(admin.ModelAdmin):
#     list_display=('id','product', 'quantity',)
    
class BadgeDisplay(admin.ModelAdmin):
    list_display=('id','name', 'code', 'code_price')

class Badge_Sandwich_Details(admin.ModelAdmin):
    list_display=('id','name', 'code', 'code_price')
    
class DiscountDisplay(admin.ModelAdmin):
    list_display=('id','product', 'code_price')

admin.site.register(Contact, ContactDetails)
admin.site.register(Category, CategoryDetails)
admin.site.register(Product, ProductDetails)
admin.site.register(Sandwich, SandwichDeatils)
admin.site.register(Southindian, SouthindianDeatils)
admin.site.register(Pizza, PizzaDeatils)
admin.site.register(Burger, BurgerDeatils)
admin.site.register(Roll, RollDeatils)
admin.site.register(FingerFood, FingerFoodDeatils)
admin.site.register(Dessert, DessertDeatils)
admin.site.register(Beverage, BeverageDeatils)
admin.site.register(Sauce, SauceDeatils)
admin.site.register(Soups, SoupsDeatils)


# admin.site.register(CartItem, CartItemsDisplay)
admin.site.register(Cart)
admin.site.register(Feedback)
admin.site.register(Order)
admin.site.register(Badge,BadgeDisplay)
admin.site.register(Badge_Sandwich,Badge_Sandwich_Details)


admin.site.register(Discount, DiscountDisplay)



