from tkinter import CASCADE
from turtle import ondrag
from django.db import models

# Create your models here.

# class Promotions(models.Model):
#     description = models.CharField(max_length=255)
#     discount = models.FloatField()
#     #product_set as enitity name

# class Product(models.Model):
#     title = models.CharField(max_length=255)  # varchar of 255
#     description = models.TextField()
#     slug = models.SlugField()
#     # maximum price can be 9999.99 
#     unit_price = models.DecimalField(max_digits=6, decimal_places=2)
#     inventory = models.IntegerField()
#     last_update = models.DateTimeField(auto_now=True)
#     collection = models.ForeignKey('Collection', on_delete=models.PROTECT)
#     promotions = models.ManyToManyField(Promotions)





# class OrderItem(models.Model):
#     quantity = models.PositiveSmallIntegerField()
#     unit_price = models.DecimalField(max_digits=6,decimal_places=2)
#     order = models.ForeignKey('Order',on_delete=models.PROTECT)
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)

# class Cart(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)


# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveSmallIntegerField()


# class Order(models.Model):
#     PAYMENT_PENDING = 'P'
#     PAYMENT_COMPLETE = 'C'
#     PAYMENT_FAILED = 'F'

#     PAYMENT_STATUS = [
#         (PAYMENT_PENDING,'Pending'),
#         (PAYMENT_COMPLETE,'Complete'),
#         (PAYMENT_FAILED,'Failed')
#     ]
#     placed_at = models.DateTimeField(auto_now_add=True)
#     payment_status = models.CharField(max_length=1,choices = PAYMENT_STATUS,default=PAYMENT_PENDING)
#     customer = models.ForeignKey('Customer', on_delete=models.PROTECT)



# class Customer(models.Model):
#     MEMBERSHIP_BRONGE = 'B'
#     MEMBERSHIP_SILVER = 'S'
#     MEMBERSHIP_GOLD = 'G'

#     MEMBERSHIP_CHOICES = [
#         (MEMBERSHIP_BRONGE,'Bronge'),
#         (MEMBERSHIP_SILVER,'Silver'),
#         (MEMBERSHIP_GOLD,'Gold')
#     ]
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=255)
#     birth_date = models.DateField(null=True)
#     membership = models.CharField(max_length=1, choices = MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONGE)
    






# class Address(models.Model):
#     street = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     cutomer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key= True)
#     zip = models.CharField(max_length=255, null=True)


# class Collection(models.Model):
#     name = models.CharField(max_length=255)
#     featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True,related_name='+')
#     # image = models.ImageField()
