from Apps.shoppingitems.models import *


# Create your models here.


class WomenDresesItems(models.Model):

    SizeChart = (
        (1,"S"),
        (2, "M"),
        (3, "L"),
        (4, "XL"),
        (5, "XXL"),

    )
    dress_name = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.SmallIntegerField(choices=SizeChart,null=True)
    price = models.DecimalField( max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='women_dress/',blank=True,null=True)
    category = models.ForeignKey(Womendress,on_delete=models.CASCADE)


    def __str__(self):
        return self.dress_name

