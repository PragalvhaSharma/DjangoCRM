#Defines the data models (i.e., the database schema). Models are classes that define 
# the structure of your database tables and how they are related.

from django.db import models

# Create your models here.

#this table name is 
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    
    def _str_(self):
        return (f"{self.first_name} {self.last_name} {self.email} {self.phone} {self.address} {self.city} {self.state} {self.zip_code}")
    