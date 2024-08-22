from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path("", login_user, name="login_user"),
    path("home", home, name="home"),
    path("about", about, name="about"),
    path("header", header, name="header"),
    path("contact_us", contact_us, name="contact_us"),
    path("bad_request", bad_request, name="404"),
    # path("login_user", login_user, name="login_user"),
    path("register_user", register_user, name="register_user"),
    path("register_success", register_success, name="register_success"),
    path("logout_user", logout_user, name="logout_user"),
    path("services", services, name="services"),
    path("cuisines", cuisines, name="cuisines"),
    path("insert_product", insert_product, name="insert_product"),
    path("feedback", feedback, name="feedback"),
    path("sandwich", sandwich, name="sandwich"),
    path("southindian", southindian, name="southindian"),
    path("pizza", pizza, name="pizza"),
    path("burger", burger, name="burger"),
    path("roll", roll, name="roll"),
    path("dessert", dessert, name="dessert"),
    path("beverage", beverage, name="beverage"),
    path("sauce", sauce, name="sauce"),
    path("soups", soups, name="soups"),
    path("fingerfood", fingerfood, name="fingerfood"),
    path('cart', cartView, name="cart"),
    path('checkout', checkoutView, name="checkout"),
]

