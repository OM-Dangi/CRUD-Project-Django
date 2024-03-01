from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=150)
    description= models.TextField()
    due_date=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=20,default='pending')
    completed=models.BooleanField(default=False)
    

    def __str__(self):
        return self.title


    