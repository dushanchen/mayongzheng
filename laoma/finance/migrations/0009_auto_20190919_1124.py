# Generated by Django 2.0.4 on 2019-09-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_auto_20190825_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment_num',
            field=models.IntegerField(default=0, verbose_name='评论量'),
        ),
    ]
