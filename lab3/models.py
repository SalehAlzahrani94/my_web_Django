from django.db import models
import datetime
class books(models.Model):
    title = models.CharField(max_length=2048) 
    description = models.TextField()
    created_at = datetime.date.today()   
    image = models.ImageField(null=True , blank=True , upload_to="images/")    # if user dident add photo true ( okay)
       
# Create your models here.
