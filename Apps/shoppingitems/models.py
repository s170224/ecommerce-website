from django.db import models

# Create your models here.



class ShoppingCategory(models.Model):
    category = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.category


class Womendress(models.Model):
    dress_model_type = models.CharField(max_length=500)
    image = models.ImageField(upload_to='womensubcategory/',null=True,blank=True)
    category =models.ForeignKey(ShoppingCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.dress_model_type



class Boysdress(models.Model):
    dress_model_type = models.CharField(max_length=500)
    category = models.ForeignKey(ShoppingCategory,on_delete=models.CASCADE)

    def __str__(self):
        return  self.dress_model_type


class Kidsdress(models.Model):
    dress_model_type = models.CharField(max_length=500)
    category = models.ForeignKey(ShoppingCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.dress_model_type








