from django.db import models

# Create your models here.

class SimpleForm(models.Model):
    id = models.BigAutoField(unique=True, primary_key= True) # Auto creator/incrementor field
    name = models.CharField(max_length=20,unique=True)
    address = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    
    def __unicode__(self):
        return u'%s' % (self.id)
