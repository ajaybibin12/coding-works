from distutils.command.upload import upload
from pickle import TRUE
from unicodedata import name
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Jharkhand','Jharkhand'),
    ('Kerala','Kerala'),
    ('Tamil nadu','Tamil nadu'),
    ('Madhya Pradesh','Madhya Pradesh'),
)
class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top wear'),
    ('BW','Bottom wear')
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    descirption=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICE=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class Order_placed(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateField(auto_now_add=TRUE)
    status=models.CharField(max_length=50,choices=STATUS_CHOICE,default='pending')
