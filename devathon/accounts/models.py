from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_num = models.CharField(max_length=20, default="")
    
    def __str__(self):
        return self.registration_num
    
    def save(self):
        super().save()