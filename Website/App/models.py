from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.template import Context, Template
from decimal import Decimal

# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class Category(models.Model):
    """A category of products."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Badge(models.Model):
    
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=700, default='<h5><span class="badge bg-primary ms-2">New</span></h5>')
    code_price = models.CharField(max_length=700, default='<s>{{product.price | safe}}</s><strong class="ms-2 text-danger">{{product.get_price_with_discount | safe}}</strong>')
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='badges')
    
    def __str__(self):
        return self.name
    
class Badge_Sandwich(models.Model):
    
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=700, default='<h5><span class="badge bg-primary ms-2">New</span></h5>')
    code_price = models.CharField(max_length=700, default='<s>{{sandwich.price | safe}}</s><strong class="ms-2 text-danger">{{sandwich.get_price_with_discount | safe}}</strong>')
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='badges')
    
    def __str__(self):
        return self.name         

class Product(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='/static/img/404.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name= "products")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'product': self}))
    
class Sandwich(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "sandwichs")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'sandwich': self}))
    

class Southindian(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "southindian")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'southindian': self}))
    
class Pizza(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "pizza")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'pizza': self}))

class Burger(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "burger")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'burger': self}))

class Beverage(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "beverage")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'beverage': self}))
    
class Dessert(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "dessert")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'dessert': self}))

class FingerFood(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "fingerfood")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'fingerfood': self}))

class Roll(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "roll")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'roll': self}))
    
class Soups(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "soups")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'soups': self}))
    
class Sauce(models.Model):
    """A product."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/' , default='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Badge_Sandwich, on_delete=models.CASCADE, related_name= "sauce")
    
    def get_price_with_discount(self):
        discount = (self.price) * Decimal(10 / 100)
        return round(self.price - discount,2)
    
    def render_code_price(self):
        template = Template(self.type.code_price)
        return template.render(Context({'sauce': self}))

class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reverse")
    code_price = models.CharField(max_length=700, default='<s>{{product.price | safe}}</s><strong class="ms-2 text-danger">{{product.get_price_with_discount() | safe}}</strong>')
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reverse")
    items = models.JSONField(default=None)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reverse2")
    address = models.TextField()
    products = models.TextField(default=None)
    payment = models.TextField()
    cost = models.IntegerField()

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reverse3")
    feedback = models.TextField()
    rating = models.IntegerField()