# Generated by Django 3.0 on 2021-04-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0003_auto_20210424_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extpro',
            name='impf',
            field=models.ImageField(default='quots.png', upload_to='pro/'),
        ),
    ]
