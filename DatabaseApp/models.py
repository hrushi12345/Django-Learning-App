from django.db import models

# Create your models here.

class Employee(models.Model):
    employeeID = models.IntegerField(unique=True, primary_key= True)
    employeeName = models.CharField(max_length=100,unique=True)
    dob = models.DateField()
    department_Key = models.ForeignKey('Department', null=True, 
                on_delete=models.SET_NULL)
    employeeEmail = models.EmailField(unique=True)

    class Meta:
        unique_together = ('employeeID','department_Key')
        
    def __unicode__(self):
        return u'%s' % (self.employeeID)

class Department(models.Model):
    departmentKey = models.IntegerField(unique=True, primary_key= True)
    departmentName = models.CharField(max_length=100,unique=True)

    def __unicode__(self):
        return u'%s' % (self.departmentKey)
