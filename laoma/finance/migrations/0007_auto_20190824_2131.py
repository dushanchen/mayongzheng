# Generated by Django 2.1 on 2019-08-24 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20190824_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='phone',
            field=models.CharField(max_length=30, null=True, verbose_name='页面底部的联系电话'),
        ),
        migrations.AlterField(
            model_name='config',
            name='beian',
            field=models.CharField(max_length=30, null=True, verbose_name='页面底部的备案号'),
        ),
    ]