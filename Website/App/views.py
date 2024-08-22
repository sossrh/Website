import logging
from django.forms import ValidationError
from django.http import HttpResponseRedirect,Http404, HttpResponse
from django.shortcuts import  render, redirect
from App.models import *
from django.db.models import *
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def home (request):
    return render(request, "home.html")

def about (request):
    return render(request,"about.html")

def header(request):
    return render(request, "header.html")

def bad_request(request):
    return render(request, "404.html")

def register_success(request):
    return render(request, "register_success.html")

def cuisines(request):
    return render(request, "cuisines.html")

# Exempt csrf protection
@csrf_exempt
def sandwich(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:   
            redirect('/login')
    # Fetch all products from the Product model
    sandwichs = Sandwich.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        'sandwichs': sandwichs,
    }
    # Render the "sandwich.html" template with the context data
    return render(request, "sandwich.html", context)
@csrf_exempt
def southindian(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
              # Fetch all products from the Product model
    sandwichs = Southindian.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        'southindiandata': sandwichs,
    }
    # Render the "sandwich.html" template with the context data
    return render(request, "southindian.html", context)


@csrf_exempt
def pizza(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
    sandwichs = Pizza.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        'pizzas': sandwichs,
    }
    # Render the "sandwich.html" template with the context data
    return render(request, "pizza.html", context)

@csrf_exempt
def burger(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
    sandwichs = Burger.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        'burgers': sandwichs,
    }
    # Render the "sandwich.html" template with the context data
    return render(request, "burger.html", context)


@csrf_exempt
def roll(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
    sandwichs = Roll.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        'rolls': sandwichs,
    }
    # Render the "sandwich.html" template with the context data
    return render(request, "roll.html", context)

@csrf_exempt
def dessert(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
    return render(request, "dessert.html")

@csrf_exempt
def beverage(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
    return render(request, "beverage.html")

@csrf_exempt
def sauce(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
    return render(request, "sauce.html")

@csrf_exempt
def soups(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
    sandwichs = Soups.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        'soupstype': sandwichs,
    }
    # Render the "sandwich.html" template with the context data
    return render(request, "soups.html", context)

@csrf_exempt
def fingerfood(request):
    if (request.method == "POST"):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
        except User.DoesNotExist:
            redirect('/login')
    sandwichs = FingerFood.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        'fingerfoods': sandwichs,
    }
    # Render the "sandwich.html" template with the context data
    return render(request, "fingerfood.html", context)

@csrf_exempt
def cartView(request):
    if (request.method == "GET"):
        # Get username from login
        username = User.objects.get(username=request.user.username)
        # Check if user has a cart
        if not Cart.objects.filter(user=username).exists():
            # Create a new cart
            new_cart = Cart(user=username, items="{}")
            new_cart.save()
        # Get cart
        cart = Cart.objects.get(user=username)
        all_items = json.loads(cart.items)
        total = 0
        items = []
        for item in all_items:
            print(item)
            # Get item price from products table
            product = Product.objects.get(name=item)
            # Get item price from products table
            price = product.price
            # Get item name from products table
            name = product.name
            # Get item image from products table
            image = product.image.url
            extension = image.split(".")[1]
            image = image.split("_")[0]
            image = image + "." + extension
            # Get item quantity from products table
            quantity = all_items[item]
            total += (price * quantity)
            # Create a dictionary to pass data to the template
            items.append({
                'name': name,
                'price': int(price*quantity),
                'image': image,
                'quantity': quantity,
            })
        # Create a context dictionary to pass data to the template
        context = {
            'cart': items,
            'total': total,
        }
        # Render the "cart.html" template with the context data
        return render(request, "cart.html", context)
    elif (request.method == 'POST'):
        item = request.POST["item"]
        action = request.POST["action"]
        try:
            # Get username from login
            username = User.objects.get(username=request.user.username)
            # Check if user has a cart
            if not Cart.objects.filter(user=username).exists():
                # Create a new cart
                new_cart = Cart(user=username, items="{}")
                new_cart.save()
            # Get cart
            cart = Cart.objects.get(user=username)
            # Check if item is already in cart
            if action == "add":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    # Increase quantity
                    all_items[item] += 1
                    cart.items = json.dumps(all_items)
                    cart.save()
                else:
                    # Add item to cart
                    all_items[item] = 1
                    cart.items = json.dumps(all_items)
                    cart.save()
            elif action == "remove":
                all_items = json.loads(cart.items)
                item_keys = all_items.keys()
                # Check if item is already in cart
                if item in item_keys:
                    quantity = all_items[item]
                    if quantity > 1:
                        all_items[item] -= 1
                        cart.items = json.dumps(all_items)
                        cart.save()
                    else:
                        del all_items[item]
                        cart.items = json.dumps(all_items)
                        cart.save()
                else:
                    return HttpResponse(status=403)
            return redirect('/cart')
        except User.DoesNotExist:   
            redirect('/login') 



@csrf_exempt
def checkoutView(request):
    if (request.method == "POST"):
        # Get username from login
        username = User.objects.get(username=request.user.username)
        # Check if user has a cart
        if not Cart.objects.filter(user=username).exists():
            # Create a new cart
            new_cart = Cart(user=username, items="{}")
            new_cart.save()
        # Get cart
        cart = Cart.objects.get(user=username)
        all_items = json.loads(cart.items)
        total = 0
        for item in all_items:
            product = Product.objects.get(name=item)
            price = product.price
            quantity = all_items[item]
            total += (price * quantity)
        keys = all_items.keys()
        if (len(keys) < 1):
            return render(request, 'checkout.html', {'error': 'No items found in cart..', 'success': False, 'total': total})
        else:
            address = request.POST['address']
            payment_method = request.POST['paymentMethod']
            totalAmt = float(request.POST['total'])
            # convert totalAmt to integer
            totalAmt = int(totalAmt)
            products = ", ".join(keys)
            order = Order.objects.create(user=username, products=products, address=address, payment=payment_method, cost=totalAmt)
            order.save()
            cart.items = "{}"
            cart.save()
            return render(request, 'checkout.html', { 'error': 'Order placed successfully!', 'success': True, 'total': total })
    else:
        username = User.objects.get(username=request.user.username)
        cart = Cart.objects.get(user=username)
        all_items = json.loads(cart.items)
        total = 0
        for item in all_items:
            product = Product.objects.get(name=item)
            price = product.price
            quantity = all_items[item]
            total += (price * quantity)

        return render(request, 'checkout.html', {'error': False, 'success': False, 'total': total})


@csrf_exempt
def feedback(request):
    # Check if user is logged in
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                username = User.objects.get(username=request.user.username)
                rating = request.POST.get('rating')
                feedback = request.POST.get('feedback')
                feedback = Feedback(user=username, rating=rating, feedback=feedback)
                feedback.save()
                return render(request, 'feedback.html', {'success': True})
            except User.DoesNotExist:
                return redirect('/login')
        else:
            return render(request, 'feedback.html', {'success': False})
    else:
        return redirect('/login')

def logout_user(request):
    logout(request)
    return redirect('login_user')

def services(request):
    # Fetch all products from the Product model
    products = Product.objects.all()
    # discounted_price = "<s>${{product.price}}</s><strong class='ms-2 text-danger'>$50.99</strong>"
    # discounted_price = Badge.objects.all()
    
    # Create a context dictionary to pass data to the template
    context = {
        'products': products,
        # 'discounted_price' : discounted_price,
    }
    
    # Render the "services.html" template with the context data
    return render(request, "templates", context),



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Get the username from the form data
            username = form.cleaned_data['name']

            # Try to send an email with the form data
            try:
                send_mail(
                    'Contact form submission',
                    form.cleaned_data['message'],
                    form.cleaned_data['email'],
                    ['sagnikdey3129.com'],
                )
            except Exception as e:
                logging.error('Error sending email: %s', str(e))

            # Display a success message to the user
            return render(request, 'contact_us_success.html', {'username': username})
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact_us.html', context)



def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('404')
    else:
        return render(request, "login.html")



def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        
        if password != confirm_password:
            context = {
                'username': username,
                'email': email,
                'error_message': "The two passwords must match."
            }
            return render(request, "register.html", context)

        user = User.objects.create_user(username, email, password)
        user.save()
        user = authenticate(username=username, password=password,)
        login(request, user)

        return redirect('register_success')
    return render(request, "register.html")






# def insert_product(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         price = request.POST.get("price")
#         image = request.POST.get("image")
#         category = request.POST.get("category")
#         form = Product(name=name, price=price, image=image, category=category)
#         form.save()
        
        
        
#     return render(request, "insert_products.html")




def insert_product(request):
    if request.method == 'POST':
        product_name = request.POST['name']
        product_price = request.POST['price']
        product_image = request.FILES['image']
        product_category = request.POST['category']
        product_type = request.POST['type']

        product = Product(
            name=product_name,
            price=product_price,
            image=product_image,
            category=Category.objects.get(id=product_category),
            type=Badge.objects.get(id=product_type)
        )
        product.save()

        return redirect('services')

    context = {
        'categories': Category.objects.all(),
        'types': Badge.objects.all()
    }
    return render(request, 'insert_products.html', context)


