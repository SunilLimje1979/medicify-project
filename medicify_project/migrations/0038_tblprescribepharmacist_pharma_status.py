# Generated by Django 5.0.1 on 2024-09-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicify_project', '0037_tblpharmacist_tbldoctorpharmacistlink_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblprescribepharmacist',
            name='pharma_status',
            field=models.IntegerField(default=0),
        ),
    ]
