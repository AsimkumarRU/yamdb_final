# Generated by Django 3.0.5 on 2020-09-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200930_0140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={
                'ordering': ['id'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={
                'ordering': ['-score'],
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews'},
        ),
        migrations.RemoveField(
            model_name='genre',
            name='title',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name='genre',
                to='api.Genre'),
        ),
    ]
