from django.db import models

# Create your models here.
class Url(models.Model):
    link=models.CharField(max_length=1000,default=None)
    url_id=models.AutoField(primary_key=True)
    short_link=models.CharField(max_length=1000)