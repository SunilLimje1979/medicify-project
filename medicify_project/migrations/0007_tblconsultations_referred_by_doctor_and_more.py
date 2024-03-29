# Generated by Django 5.0.2 on 2024-02-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicify_project', '0006_alter_tbldatacodemaster_datacodename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblconsultations',
            name='referred_by_doctor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbldoctorlocations',
            name='location_qr_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbldoctorlocations',
            name='location_token',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='tbldoctors',
            name='doctor_login_token',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='tblconsultations',
            name='referred_to_doctor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
