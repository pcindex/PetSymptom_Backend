# Generated by Django 4.1.2 on 2022-11-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_exam_comments_alter_exam_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='comments',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='heart_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='respiration_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='temperature',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
