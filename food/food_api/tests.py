from django.test import TestCase
from .models import *
from django.urls import reverse
from urllib.parse import urlencode


class FoodTest(TestCase):
    def setUp(self):
        self.kitchen = Kitchen.objects.create(kitchen_name='xyi')
        self.dish = Dish.objects.create(dish_name = 'Роллы с бульёном',
    incridients= 'fdgdhd',
    image = 'gdgdhf',
    kitchen_type = self.kitchen,
    quantity = 3,
    price = 9999,
    )
        self.user = User.objects.create(username='pidor',
    password = 'otbros228',
    image='fgdgdh',
    home_adress = 'fdggd')
        self.user.cart.set([])
     
    def test_search_dish(self):
        data = {'q': 'роллы'}
        response = self.client.get(reverse('dish-search-dish'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.dish.dish_name in response.content.decode())
        
    def test_add_to_dish(self):
        data = urlencode({'id': self.user.pk, 'q':self.dish.pk})
        response = self.client.put(reverse('user-add-to-dish'), data, content_type="application/x-www-form-urlencoded" )
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(self.dish.pk), response.content.decode())
        

# Create your tests here.
