from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.kitchen_name

class Dish(models.Model):
    dish_name = models.CharField(max_length=30)
    incridients = models.TextField()
    image = models.TextField()
    kitchen_type = models.ForeignKey(Kitchen, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=False)

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32, validators=[MinLengthValidator(8)])
    image = models.TextField(default='https://static.tildacdn.com/tild3133-6461-4762-b763-393238646435/1_9e9CY6nDatrFlVkDHW.png')
    home_adress = models.TextField()
    cart = models.ManyToManyField(Dish, blank=True)
    
    def __str__(self):
        return  self.username
    
Status = (
    ('1', 'В обработке'),
    ('2', 'Готовится '),
    ('3', 'Доставляется'),
    ('4', 'Доставлен')
    
)
    
class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    products = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    make_at = models.DateField(default=timezone.now)
    delivery_date = models.DateField()
    status = models.CharField(max_length=100, choices=Status)
    total_price = models.PositiveIntegerField(null=False)
    
# Create your models here.
