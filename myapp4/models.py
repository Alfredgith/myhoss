from django.db import models

class book(models.Model):
      title=models.CharField(max_length=20)
      time=models.DateTimeField(auto_now_add=True)
