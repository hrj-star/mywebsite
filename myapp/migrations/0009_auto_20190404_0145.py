# Generated by Django 2.1.4 on 2019-04-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190404_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='name',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
    ]
