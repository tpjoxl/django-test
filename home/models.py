from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)            #標題
    content = models.TextField(blank=True)              #內文
    photo = models.URLField(blank=True)                 #照片
    location = models.CharField(max_length=100)         #地點
    created_at = models.DateTimeField(auto_now_add=True)#建立時間
    changed_at = models.DateTimeField(auto_now=True)    #修改時間
    class Meta:
        db_table = "Post"
    
    def __str__(self):
        return self.title

class setting(models.Model):
    topic = models.CharField(max_length=100)            #標題

    def get_absolute_url(self):
        return reverse("gettopic", kwargs={"pk": self.pk})

    def __str__(self):
        return self.topic

    

    