from django.db import models

# Create your models here.
class Comment(models.Model):
    user=models.CharField(max_length=50)
    content=models.TextField( )
    def __str__(self):
        self.user+":"+self.content