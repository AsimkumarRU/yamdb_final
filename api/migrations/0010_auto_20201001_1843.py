# Generated by Django 3.0.5 on 2020-10-01 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201001_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews'},
        ),
    ]
