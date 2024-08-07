# Generated by Django 3.2.4 on 2024-08-06 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20240730_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.TextField(choices=[('Greece', 'GREECE'), ('Spain', 'SPAIN'), ('Italy', 'ITALY'), ('England', 'ENGLAND')], default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='post',
            name='theme',
            field=models.CharField(choices=[('Beach', 'BEACH'), ('Barn', 'BARN'), ('Classic', 'CLASSIC'), ('Rustic', 'RUSTIC'), ('Fairytale', 'FAIRYTALE')], default='', max_length=9),
        ),
    ]
