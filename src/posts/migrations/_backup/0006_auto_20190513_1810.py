# Generated by Django 2.2 on 2019-05-13 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190511_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='Post',
            name='body',
            field=models.TextField(null=True),  # unique=True
            preserve_default=False,
        ),
    ]



