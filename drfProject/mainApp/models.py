from django.db import models

# Create your models here.

# 간단하게 제목, 내용, 업데이트 된 날짜 담은 모델을 생성함
class Review(models.Model):
    title = models.CharField(max_length=50) #제목
    content = models.TextField() #내용
    updated_at = models.DateTimeField(auto_now=True) #업데이트 된 날짜