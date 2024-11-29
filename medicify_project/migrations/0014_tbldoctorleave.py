# Generated by Django 5.0.2 on 2024-03-11 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicify_project', '0013_consultationfee_avg_time_per_patient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbldoctorleave',
            fields=[
                ('doctor_leave_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('day', models.IntegerField()),
                ('leave_date', models.BigIntegerField()),
                ('order', models.IntegerField()),
                ('updated_date', models.BigIntegerField()),
                ('start_time', models.IntegerField()),
                ('end_time', models.IntegerField()),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by', models.IntegerField(blank=True, null=True)),
                ('deleted_by', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctorleave_doctor_id', to='medicify_project.tbldoctors')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctorleave_location_id', to='medicify_project.tbldoctorlocations')),
            ],
            options={
                'db_table': 'tbldoctorleave',
                'managed': True,
            },
        ),
    ]
