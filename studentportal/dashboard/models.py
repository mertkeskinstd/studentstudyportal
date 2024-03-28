from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    
    class Meta:
        verbose_name="Notes"
        verbose_name_plural="Notes"
        
    
    def __str__(self) :
        return self.title
    
    

class Homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.TextField()
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)
    def __str__(self) :
        return self.title
    def save(self, *args, **kwargs):
        if not self.pk:  # Eğer nesne yeni oluşturuluyorsa (yani henüz bir primary key'e sahip değilse)
            self.due = timezone.now()  # Şu anki zamanı atama yap
        super().save(*args, **kwargs)
    
    
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)
    class Meta:
        verbose_name="Todo"
        verbose_name_plural="Todo"
    def __str__(self) :
        return self.title
        