# Generated by Django 4.1.2 on 2022-11-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='comments',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='exam',
            name='cost',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='exam',
            name='heart_rate',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='respiration_rate',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='temperature',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pets',
            name='conditions',
            field=models.ManyToManyField(blank=True, to='api.conditions'),
        ),
    ]
