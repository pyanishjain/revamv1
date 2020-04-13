from django.db import models

# Create your models here.3


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="Shop/images", null=True, blank=True)

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount =models.IntegerField(null=True, blank=True, default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100, null=True, blank=True)
    shop_type = models.CharField(max_length=100, null=True, blank=True)
    shop_area = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)