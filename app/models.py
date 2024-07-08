from django.db import models

# Create your models here.


class Product_Category(models.Model):
    category_name=models.CharField(max_length=100,primary_key=True)
    category_id=models.IntegerField()

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category_name=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    pid=models.IntegerField()
    pname=models.CharField(max_length=100)
    pprice=models.IntegerField()
    pdate=models.DateField()

    def __str__(self):
        return self.pname