from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

# A_TYPE = [(0, '信托'),(1, '定融工具'),(2,),()]

class Article(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '文章'

    title = models.CharField(max_length=100, verbose_name='标题')
    user = models.CharField(max_length=100,  verbose_name='作者', null=True)
    cover = models.ImageField(upload_to='cover', null=True, verbose_name='封面')
    read = models.IntegerField(default=0, verbose_name='阅读量')
    comment_num = models.IntegerField(default=0, verbose_name='阅读量')

    type = models.IntegerField(default=0, choices=[(0, '文章'),(1, '资讯')])
    top = models.IntegerField(default=10000,verbose_name='置顶参数(越小越靠顶,10000表示未发布)')

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content = UEditorField(width=1200, height=1200, toolbars="full", imagePath="images/", filePath="files/",\
         upload_settings={"imageMaxSize":120400000}, settings={}, verbose_name='内容', null=True)

    

    def __str__(self):
        return self.title


class Comment(models.Model):
    
    user = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=100)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)