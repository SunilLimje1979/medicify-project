# Generated by Django 5.0.1 on 2024-06-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicify_project', '0028_tblpatientdoctorlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblpatientdoctorlink',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]
