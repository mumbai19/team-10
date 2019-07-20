from django.db import models
import random
import os
import pyimgur
import requests
import json

PRODUCT_CATEGORY_CHOICES=(
('Bags','Bags'),
('Keychains','Keychains'),
('Bookmarks', 'Bookmarks'),
('Paperweights', 'Paperweights'),
('Greetings Cards','Greetings Cards'),
('Candles','Candles'),
('Jewellery','Jewellery'),
('Others','Others'),
)

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance, filename):
<<<<<<< HEAD
    new_filename = random.randint(1000,9999)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename , ext = ext)
    return 'products/{new_filename}/{final_filename}'.format(
                        new_filename = new_filename,
                        final_filename = final_filename
                        )
class ProductManager(models.Manager):
    def get_by_id(self ,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

    def bags(self):
        return self.filter(category='Bags')

    def keychains(self):
        return self.filter(category='Keychains')

    def bookmarks(self):
        return self.filter(category='Bookmarks')

    def paperweights(self):
        return self.filter(category='Paperweights')

    def cards(self):
        return self.filter(category='Greeting Cards')

    def candles(self):
        return self.filter(category='Candles')

    def jewellery(self):
        return self.filter(category='Jewellery')
        
=======
    URL = "https://api.imgur.com/3/upload"
    headers = {'Content-Type':  'application/json',
      'Authorization': 'Client-ID 3f40f86eef92465'}
    with open(filename, 'rb') as f:
        payload = {'data':f}
        r = requests.post(URL,data=json.dumps(payload),headers=headers)
    print("data is ",r.json())
>>>>>>> f7418790d69847895a22b162e0496b7391061c6a

class Product(models.Model):
    title             = models.CharField(max_length = 120)
    description       = models.TextField()
    category          = models.CharField(max_length = 20, default = 'others', choices=PRODUCT_CATEGORY_CHOICES)
    price             = models.DecimalField(max_digits = 10, decimal_places = 2, default = 2000.00)
    in_stock          = models.BooleanField(default=True)
    image             = models.ImageField(upload_to = upload_image_path,null =True, blank = True)

    objects = ProductManager()

    def __str__(self):
        return str(self.title)
