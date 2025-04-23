from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    size=models.CharField(max_length=200)
    description=models.CharField(max_length=500,default=None)
    price=models.FloatField(null=True,blank=True)
    image_url=models.CharField(max_length=2083,default=False)
    follow_products=models.CharField(max_length=2083,blank=True)
    product_available=models.BooleanField(default=False)


class Order(models.Model):
    product=models.ForeignKey(Post,max_length=200,null=True,blank=True,on_delete=models.SET_NULL)
    created=models.DateTimeField(auto_now_add=True)


