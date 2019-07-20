from django.db import models
import random
import os

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
    URL = "https://api.imgur.com/3/upload"
    headers = {'Content-Type':  'application/json',
      'Authorization': 'Client-ID 3f40f86eef92465'}
    with open(filename, 'rb') as f:
        payload = {'data':f}
        r = requests.post(URL,data=json.dumps(payload),headers=headers)
    print("data is ",r.json())

class Product(models.Model):
    title             = models.CharField(max_length = 120)
    description       = models.TextField()
    category          = models.CharField(max_length = 20, default = 'others', choices=PRODUCT_CATEGORY_CHOICES)
    price             = models.DecimalField(max_digits = 10, decimal_places = 2, default = 2000.00)
    in_stock          = models.BooleanField(default=True)
    image             = models.ImageField(upload_to = upload_image_path,null =True, blank = True)

  # objects = ProductManager()

    def __str__(self):
        return str(self.title)
