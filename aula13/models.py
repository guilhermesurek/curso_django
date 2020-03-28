from django.db import models

# Create your models here.

class UploadFile(models.Model):
    name = models.CharField(max_length=30)
    file = models.ImageField(upload_to='uploads')