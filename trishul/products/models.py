from django.db import models
import random
import os

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
    new_filename = random.randint(1000,9999)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename , ext = ext)
    return 'products/{new_filename}/{final_filename}'.format(
                        new_filename = new_filename,
                        final_filename = final_filename
                        )

class Product(models.Model):
    title             = models.CharField(max_length = 120)
    description       = models.TextField()
    category          = models.CharField(max_length = 20, default = 'others', choices=PRODUCT_CATEGORY_CHOICES)
    price             = models.DecimalField(max_digits = 10, decimal_places = 2, default = 2000.00)
    in_stock          = models.BooleanField(default=True)
    image             = models.ImageField(upload_to = upload_image_path,null =True, blank = True)

    def __str__(self):
        return str(self.title)
