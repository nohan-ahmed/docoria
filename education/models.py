from django.db import models
from accounts.models import User
from core.models import Country
from .constraints import DEGREE_TYPE
# Create your models here.
class Education(models.Model):
    user = models.ForeignKey(to=User, related_name='education' , on_delete=models.CASCADE)
    country = models.OneToOneField(to=Country, on_delete=models.CASCADE)
    institution = models.CharField(max_length=250)
    degree = models.CharField(choices=DEGREE_TYPE,max_length=250)
    field_of_study = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    gpa = models.DecimalField(max_digits=2, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.degree} {self.field_of_study} - {self.gpa}'