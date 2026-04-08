from django.db import models
class employee(models.Model):
    emp_id=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=30)
    emp_salary=models.FloatField()
# Create your models here.
