from django.db import models
from datetime import date

class Contact(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    last_name=models.CharField(max_length=50,null=False,blank=False)
    phone=models.CharField(max_length=12,blank=True,null=True)
    mobile=models.CharField(max_length=12,blank=False,null=False)
    company=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField()
    date=models.DateField(default=date.today)
    notes=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


