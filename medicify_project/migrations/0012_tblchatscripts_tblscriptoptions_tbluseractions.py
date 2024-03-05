# Generated by Django 5.0.2 on 2024-03-05 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicify_project', '0011_rename_unique_location_token_constraint_tbldoctorlocations_location_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblChatScripts',
            fields=[
                ('Script_id', models.AutoField(primary_key=True, serialize=False)),
                ('Script_Code', models.IntegerField(blank=True, null=True)),
                ('Script_Type', models.IntegerField(blank=True, null=True)),
                ('Script_Language', models.CharField(blank=True, max_length=2, null=True)),
                ('Script_Text', models.TextField(blank=True, null=True)),
                ('S1', models.IntegerField(blank=True, null=True)),
                ('S2', models.IntegerField(blank=True, null=True)),
                ('created_on', models.IntegerField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.IntegerField(blank=True, null=True)),
                ('last_modified_by', models.IntegerField(blank=True, null=True)),
                ('deleted_by', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('Location_token', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicify_project.tbldoctorlocations', to_field='location_token')),
            ],
            options={
                'db_table': 'tblChatScripts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='tblScriptOptions',
            fields=[
                ('Script_Option_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Script_Option_Type', models.IntegerField(blank=True, null=True)),
                ('Script_Option_Langauge', models.CharField(blank=True, max_length=2, null=True)),
                ('Script_Option_Text', models.TextField(blank=True, null=True)),
                ('Script_Option_Value', models.CharField(blank=True, max_length=10, null=True)),
                ('Script_Option_Action_Script_Id', models.IntegerField(blank=True, null=True)),
                ('created_on', models.IntegerField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.IntegerField(blank=True, null=True)),
                ('last_modified_by', models.IntegerField(blank=True, null=True)),
                ('deleted_by', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('Location_token', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicify_project.tbldoctorlocations', to_field='location_token')),
                ('Script_Code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicify_project.tblchatscripts')),
            ],
            options={
                'db_table': 'tblScriptOptions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='tblUserActions',
            fields=[
                ('Action_Id', models.AutoField(primary_key=True, serialize=False)),
                ('User_Id', models.IntegerField(blank=True, null=True)),
                ('Script_Option_Id', models.IntegerField(blank=True, null=True)),
                ('Script_Option_Langauge', models.CharField(blank=True, max_length=2, null=True)),
                ('Script_Action_Input', models.CharField(blank=True, max_length=100, null=True)),
                ('Script_Option_Value', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.IntegerField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.IntegerField(blank=True, null=True)),
                ('last_modified_by', models.IntegerField(blank=True, null=True)),
                ('deleted_by', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('Location_token', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicify_project.tbldoctorlocations', to_field='location_token')),
                ('Script_Code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicify_project.tblchatscripts')),
            ],
            options={
                'db_table': 'tblUserActions',
                'managed': True,
            },
        ),
    ]