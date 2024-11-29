# Generated by Django 5.0.1 on 2024-06-04 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicify_project', '0026_tbldatacodemaster_doctor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblMasterAllergies',
            fields=[
                ('allergy_id', models.AutoField(primary_key=True, serialize=False)),
                ('allergy_name', models.CharField(max_length=100)),
                ('allergy_type', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by', models.IntegerField(blank=True, null=True)),
                ('deleted_by', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterallergy_doctor_id', to='medicify_project.tbldoctors')),
            ],
            options={
                'db_table': 'tblMasterAllergies',
            },
        ),
        migrations.CreateModel(
            name='tblMasterDisease',
            fields=[
                ('disease_id', models.AutoField(primary_key=True, serialize=False)),
                ('disease_name', models.CharField(max_length=100)),
                ('disease_type', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by', models.IntegerField(blank=True, null=True)),
                ('deleted_by', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterdisease_doctor_id', to='medicify_project.tbldoctors')),
            ],
            options={
                'db_table': 'tblMasterDisease',
            },
        ),
        migrations.CreateModel(
            name='tblPatientAllergies',
            fields=[
                ('patient_allergy_id', models.AutoField(primary_key=True, serialize=False)),
                ('allergy_entry_date', models.BigIntegerField()),
                ('allergy_details', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by', models.IntegerField(blank=True, null=True)),
                ('deleted_by', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('allergy_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientallergy_disease_id', to='medicify_project.tblmasterallergies')),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientallergy_patient_id', to='medicify_project.tblpatients')),
            ],
            options={
                'db_table': 'tblPatientAllergies',
            },
        ),
        migrations.CreateModel(
            name='tblPatientDisease',
            fields=[
                ('patient_disease_id', models.AutoField(primary_key=True, serialize=False)),
                ('disease_entry_date', models.BigIntegerField()),
                ('disease_details', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by', models.IntegerField(blank=True, null=True)),
                ('deleted_by', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('disease_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientdisease_disease_id', to='medicify_project.tblmasterdisease')),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientdisease_patient_id', to='medicify_project.tblpatients')),
            ],
            options={
                'db_table': 'tblPatientDisease',
            },
        ),
    ]
