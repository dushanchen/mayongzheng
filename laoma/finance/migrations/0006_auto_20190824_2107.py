# Generated by Django 2.1 on 2019-08-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20190824_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='beian',
            field=models.CharField(max_length=30, null=True, verbose_name='备案号'),
        ),
        migrations.AddField(
            model_name='config',
            name='version',
            field=models.CharField(max_length=30, null=True, verbose_name='页面底部的版权'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.IntegerField(choices=[(0, '信托文章'), (1, '定容工具'), (2, '行业资讯')], default=0, verbose_name='文章类型'),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(max_length=100, null=True, verbose_name='网站url( 带上http:// 或者 '),
        ),
    ]
