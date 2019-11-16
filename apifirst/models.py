from django.db import models

# Create your models here.

class employee(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    empid=models.PositiveIntegerField()

    def __str__(self):
        return str(self.firstname)+"_______"+str(self.empid)

