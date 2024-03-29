# Generated by Django 2.1 on 2019-08-24 20:32

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20190824_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='config', verbose_name='顶部logo')),
                ('ma1', models.ImageField(null=True, upload_to='config', verbose_name='微信二维码1')),
                ('ma2', models.ImageField(null=True, upload_to='config', verbose_name='微信二维码2')),
            ],
            options={
                'verbose_name': '配置',
                'verbose_name_plural': '配置',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='网站名')),
                ('url', models.CharField(max_length=100, null=True, verbose_name='网站url')),
            ],
            options={
                'verbose_name': '外链',
                'verbose_name_plural': '外链',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(null=True, verbose_name='文章内容(备注:按钮上传图片)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='top',
            field=models.IntegerField(default=10000, verbose_name='置顶参数(越小越靠顶,10000表示未发布, 要发布就改小)'),
        ),
    ]
