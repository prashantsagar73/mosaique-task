from django.db import models

# Create your models here.
class Weather(models.Model):
    # id = models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    temprature = models.CharField(max_length=200)
    time_stamp = models.DateField(auto_now_add=True)
    wather_name= models.CharField(max_length=100)
    images = models.ImageField(upload_to='gallery',null=True,blank=True)



    def __str__(self):
        return f'{self.temprature}'