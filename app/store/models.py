from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    """create customer model based on the default user"""

    user = models.OneToOneField(User, on_delete=models.CASCADE,
    null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """create product & check if it digital or not"""

    name = models.CharField(max_length=255, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/roducts')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        """this method check if product has image or not"""
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    """add order with transaction id to follow it"""

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
    blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        """check if the product is digital or not"""
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        """calculate the total price int the whole cart"""
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        """claculate the total for specific item"""
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    """add order items with it's detail"""

    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
    blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
    blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        """claculate the total for specific item"""
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product.name

class ShippingAddress(models.Model):
    """add order information and address"""

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
    blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
    blank=True, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
