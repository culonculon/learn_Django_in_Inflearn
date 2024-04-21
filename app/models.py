from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)  # 길이 제한 있음
    content = models.TextField()  # 길이 제한 없음
