from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

# A_TYPE = [(0, '信托'),(1, '定融工具'),(2,),()]


from pyquery import PyQuery as p 


class Article(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '文章'

    title = models.CharField(max_length=100, verbose_name='标题')
    user = models.CharField(max_length=100,  verbose_name='作者', null=True)
    cover = models.ImageField(upload_to='cover', null=True, verbose_name='封面')
    read = models.IntegerField(default=0, verbose_name='阅读量')
    comment_num = models.IntegerField(default=0, verbose_name='阅读量')

    type = models.IntegerField(default=0, choices=[(0, '信托文章'),(1, '定容工具'),(2, '行业资讯')], verbose_name='文章类型')
    top = models.IntegerField(default=10000, verbose_name='置顶参数(越小越靠顶,10000表示未发布, 要发布就改小)')
    head = models.IntegerField(default=0, choices=[(0, '否'),(1, '是')], verbose_name='头条推荐')
    scroll_head = models.IntegerField(default=0, choices=[(0, '否'),(1, '是')], verbose_name='滚动头条')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True)
    content = UEditorField(width=1200, height=1200, toolbars="full", imagePath="images/", filePath="files/",\
         upload_settings={"imageMaxSize":120400000}, settings={}, verbose_name='文章内容(备注:按钮上传图片)', null=True)

    def __str__(self):
        return self.title

    def short(self):
        return p(self.content).text()[:40] if self.content else ''


class Comment(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '评论'

    user = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=100)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)


class Message(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '留言'

    user = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=100)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)



class Config(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '配置'

    logo = models.ImageField(upload_to='config', null=True, blank=True, verbose_name='顶部logo')
    ma1 = models.ImageField(upload_to='config', null=True, blank=True,verbose_name='微信二维码1')
    ma2 = models.ImageField(upload_to='config', null=True, blank=True,verbose_name='微信二维码2')

    version = models.CharField(max_length=30, null=True, blank=True,verbose_name='页面底部的版权')
    beian = models.CharField(max_length=30, null=True,blank=True, verbose_name='页面底部的备案号')
    phone = models.CharField(max_length=30, null=True,blank=True, verbose_name='页面底部的联系电话')


class Link(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '外链'

    name = models.CharField(max_length=30, null=True, verbose_name='网站名')
    url = models.CharField(max_length=100, null=True, verbose_name='网站url( 带上http:// 或者 ')
    
