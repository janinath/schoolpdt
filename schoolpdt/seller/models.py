from django.db import models

# Create your models here.
class Category(models.Model):
    c_name=models.TextField(max_length=50)
    c_image=models.ImageField(upload_to='photos/category',blank=True)
    def __str__(self):
        return self.c_name
class Product(models.Model):
    p_name=models.TextField(max_length=20)
    price=models.IntegerField()
    p_image=models.ImageField(upload_to='photos/products')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.p_name
    