# Generated by Django 5.0.2 on 2024-03-19 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicify_project', '0016_alter_tblpatientmedications_medicine_doses'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblpatientvitals',
            name='appointment_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicify_project.tbldoctorappointments'),
        ),
        migrations.AddField(
            model_name='tblpatientvitals',
            name='bmi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tblpatientvitals',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tblpatientlabinvestigations',
            name='labinvestigation_category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
