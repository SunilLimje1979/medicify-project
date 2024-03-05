# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Tbldatacodemaster(models.Model):
    datacodeid = models.AutoField( primary_key=True)  # Field name made lowercase.
    datacodename = models.CharField( max_length=256)  # Field name made lowercase.
    datacodevalue = models.CharField( max_length=256)  # Field name made lowercase.
    datacodedescription = models.TextField()  # Field name made lowercase.

    class Meta:
        db_table = 'tbldatacodemaster'

######################################Tbldoctors
class Tbldoctors(models.Model):
    doctor_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_firstname = models.CharField( max_length=50)  # Field name made lowercase.
    doctor_lastname = models.CharField( max_length=50)  # Field name made lowercase.
    doctor_mobileno = models.CharField( max_length=10)  # Field name made lowercase.
    doctor_email = models.CharField( max_length=100)  # Field name made lowercase.
    doctor_dateofbirth = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    doctor_maritalstatus = models.IntegerField()  # Field name made lowercase.
    doctor_gender = models.SmallIntegerField()  # Field name made lowercase.
    doctor_aadharnumber = models.CharField( max_length=16)  # Field name made lowercase.
    doctor_address = models.CharField( max_length=1000, blank=True, null=True)  # Field name made lowercase.
    doctor_cityid = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    doctor_stateid = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    doctor_countryid = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    doctor_pincode = models.CharField( max_length=6, blank=True, null=True)  # Field name made lowercase.
    doctor_registrationno = models.CharField(max_length=50)  # Field name made lowercase.
    doctor_profilleimageurl = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField()  # Field name made lowercase.
    doctor_login_token = models.CharField( max_length=32, blank=True, null=True) 

    class Meta:
        db_table = 'tbldoctors'


#####################################################Tblpatients
class Tblpatients(models.Model):
    patient_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    patient_mobileno = models.CharField( max_length=10)  # Field name made lowercase.
    patient_firstname = models.CharField( max_length=50)  # Field name made lowercase.
    patient_fateherhusbandname = models.CharField( max_length=50, blank=True, null=True)  # Field name made lowercase.
    patient_lastname = models.CharField( max_length=50)  # Field name made lowercase.
    patient_gender = models.SmallIntegerField()  # Field name made lowercase.
    patient_dateofbirth = models.BigIntegerField( blank=True, null=True)  # Field name made lowercase.
    patient_maritalstatus = models.IntegerField()  # Field name made lowercase.
    patient_aadharnumber = models.CharField( max_length=16, blank=True, null=True)  # Field name made lowercase.
    patient_universalhealthid = models.IntegerField()  # Field name made lowercase.
    patient_bloodgroup = models.IntegerField()  # Field name made lowercase.
    patient_level = models.CharField( max_length=1)  # Field name made lowercase.
    patient_emergencycontact = models.CharField( max_length=10)  # Field name made lowercase.
    patient_address = models.CharField( max_length=100, blank=True, null=True)  # Field name made lowercase.
    patient_cityid = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    patient_stateid = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    patient_countryid = models.IntegerField()  # Field name made lowercase.
    createdby = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    createdon = models.BigIntegerField(blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    istestpatient = models.IntegerField()  # Field name made lowercase.

    class Meta:
        db_table = 'tblpatients'
#######################################################Tblconsultations
class Tblconsultations(models.Model):
    consultation_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors,on_delete=models.SET_NULL, null=True) # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients,on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_status = models.SmallIntegerField()  # Field name made lowercase.
    consultation_datetime = models.IntegerField()  # Field name made lowercase.
    consultation_mode = models.SmallIntegerField()  # Field name made lowercase.
    visit_reason = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    consultation_duration = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    further_assited = models.IntegerField()  # Field name made lowercase.
    followup_datetime = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deleted_reason = models.CharField( max_length=100, blank=True, null=True)  # Field name made lowercase.
    instructions = models.TextField(blank=True, null=True)
    consultation_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    referred_to_doctor = models.CharField( max_length=255, blank=True, null=True)
    referred_by_doctor = models.CharField( max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'tblconsultations'


############################################################TbldoctorMedicines
class TbldoctorMedicines(models.Model):
    doctor_medicine_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    medicine_code = models.CharField( max_length=5)  # Field name made lowercase.
    medicine_name = models.CharField( max_length=100)  # Field name made lowercase.
    medicine_form = models.SmallIntegerField()  # Field name made lowercase.
    medicine_frequency = models.CharField( max_length=3)  # Field name made lowercase.
    medicine_duration = models.IntegerField()  # Field name made lowercase.
    medicine_dosages = models.CharField( max_length=100)  # Field name made lowercase.
    medicine_manufacture = models.CharField( max_length=100)  # Field name made lowercase.
    medicine_packsize = models.IntegerField()  # Field name made lowercase.
    medicine_preservation = models.IntegerField()  # Field name made lowercase.
    medicine_minstock = models.IntegerField()  # Field name made lowercase.
    medicine_gst = models.IntegerField()  # Field name made lowercase.
    medicine_content_name = models.CharField(max_length=100)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deletedreason = models.CharField( max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tbldoctor_medicines'

############################################Tbllabinvestigations
class Tbllabinvestigations(models.Model):
    investigation_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors,on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    investigation_category = models.CharField( max_length=255)  # Field name made lowercase.
    investigation_name = models.CharField( max_length=255)
    
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Tbllabinvestigations'


############################################Tbldoctorappointments
class Tbldoctorappointments(models.Model):
    appointment_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors,on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    appointment_datetime = models.BigIntegerField()  # Field name made lowercase.
    appointment_token = models.IntegerField()  # Field name made lowercase.
    appointment_name = models.CharField( max_length=100)  # Field name made lowercase.
    appointment_mobileno = models.CharField( max_length=10)  # Field name made lowercase.
    appointment_gender = models.IntegerField()  # Field name made lowercase.
    appointment_status = models.IntegerField()  # Field name made lowercase.
    consultation_id = models.ForeignKey(Tblconsultations, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField( blank=True, null=True)

    class Meta:
        db_table = 'tbldoctorappointments'

###############################################Tbldoctorlocationavailability
class Tbldoctorlocationavailability(models.Model):
    doctor_location_availability_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True) # Field name made lowercase.
    doctor_location_id = models.IntegerField()  # Field name made lowercase.
    availability_day = models.SmallIntegerField()  # Field name made lowercase.
    availability_starttime = models.CharField( max_length=8)  # Field name made lowercase.
    availability_endtime = models.IntegerField()  # Field name made lowercase.
    availability_status = models.IntegerField()  # Field name made lowercase.
    availability_order = models.IntegerField()  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deletedreason = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tbldoctorlocationavailability'

##########################################Tbldoctorlocations
class Tbldoctorlocations(models.Model):
    doctor_location_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    location_title = models.CharField(max_length=100)  # Field name made lowercase.
    location_type = models.IntegerField()  # Field name made lowercase.
    location_address = models.CharField(max_length=255)  # Field name made lowercase.
    location_latitute = models.CharField( max_length=15, blank=True, null=True)  # Field name made lowercase.
    location_longitute = models.CharField( max_length=15, blank=True, null=True)  # Field name made lowercase.
    location_city_id = models.IntegerField()  # Field name made lowercase.
    location_state_id = models.IntegerField()  # Field name made lowercase.
    location_country_id = models.IntegerField()  # Field name made lowercase.
    location_pincode = models.CharField( max_length=6)  # Field name made lowercase.
    location_status = models.IntegerField()  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deletedreason = models.CharField( max_length=200, blank=True, null=True)  # Field name made lowercase.
    location_token = models.CharField(max_length=32,blank=True,null=True,unique=True)
    location_qr_url = models.CharField( max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'tbldoctorlocations'

###################################################TblmedicineInstructions
class TblmedicineInstructions(models.Model):
    doctor_instruction_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    instruction_language = models.CharField( max_length=2)  # Field name made lowercase.
    instruction_text = models.CharField( max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'tblmedicine_instructions'

##############################################TblpateintCharges
class TblpateintCharges(models.Model):
    pateint_charges_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_status = models.IntegerField()  # Field name made lowercase.
    charges_referencetype = models.IntegerField()  # Field name made lowercase.
    charges_reference_id = models.IntegerField()  # Field name made lowercase.
    charges_type = models.IntegerField()  # Field name made lowercase.
    charges_category = models.IntegerField()  # Field name made lowercase.
    charges_notes = models.CharField( max_length=100, blank=True, null=True)  # Field name made lowercase.
    charges_units = models.IntegerField()  # Field name made lowercase.
    charges_rate = models.IntegerField()  # Field name made lowercase.
    charges_amount = models.IntegerField()  # Field name made lowercase.
    charges_discount = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    charges_discount_reason = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    charges_discountby = models.CharField( max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deleted_reason = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblpateint_charges'

################################################TblpatientComplaints
class TblpatientComplaints(models.Model):
    patient_complaint_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    complaint_datetime = models.IntegerField()  # Field name made lowercase.
    complaint_details = models.TextField()  # Field name made lowercase.
    appointment_id = models.ForeignKey(Tbldoctorappointments, on_delete=models.SET_NULL, null=True) 
    consultation_id = models.ForeignKey(Tblconsultations, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deleted_reason = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblpatient_complaints'

##################################################TblpatientFindingsandsymtoms
class TblpatientFindingsandsymtoms(models.Model):
    patient_findings_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_status = models.SmallIntegerField()  # Field name made lowercase.
    findgings_datetime = models.IntegerField()  # Field name made lowercase.
    consultation_id = models.ForeignKey(Tblconsultations, on_delete=models.SET_NULL, null=True )  # Field name made lowercase.
    findings = models.TextField()  # Field name made lowercase.
    symtoms = models.TextField()  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deleted_reason = models.CharField( max_length=100)  # Field name made lowercase.
    kco = models.CharField(blank=True, null=True)
    advice = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tblpatient_findingsandsymtoms'

##############################################Tblprescriptions
class Tblprescriptions(models.Model):
    prescriptions_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_status = models.IntegerField()  # Field name made lowercase.
    consultation_id = models.ForeignKey(Tblconsultations, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    prescription_datetime = models.IntegerField()  # Field name made lowercase.
    prescription_details = models.TextField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deleted_reason = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblprescriptions'
        
##############################################TblpatientLabinvestigations
class TblpatientLabinvestigations(models.Model):
    patient_labinvestigation_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_status = models.IntegerField()  # Field name made lowercase.
    consultation_id = models.ForeignKey(Tblconsultations, on_delete=models.SET_NULL, null=True )  # Field name made lowercase.
    prescription_id = models.ForeignKey(Tblprescriptions, on_delete=models.SET_NULL, null=True ) # Field name made lowercase.
    labinvestigation_datetime = models.IntegerField()  # Field name made lowercase.
    labinvestigation_category = models.IntegerField()  # Field name made lowercase.
    patient_labtestid = models.ForeignKey(Tbllabinvestigations, on_delete=models.SET_NULL, null=True)
    patient_labtestreport = models.CharField( max_length=100)  # Field name made lowercase.
    patient_labtestsample = models.IntegerField()  # Field name made lowercase.
    patient_labtestreport_check = models.IntegerField()  # Field name made lowercase.
    lattest_extrafield1 = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deletedon = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deleted_reason = models.CharField( max_length=100, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(default="0")  # Field name made lowercase.

    class Meta:
        db_table = 'tblpatient_labinvestigations'

##################################################TblpatientMedications
class TblpatientMedications(models.Model):
    patient_medication_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients,on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_status = models.IntegerField()  # Field name made lowercase.
    consultation_id = models.ForeignKey(Tblconsultations, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    prescription_id = models.ForeignKey(Tblprescriptions, on_delete=models.SET_NULL, null=True) # Field name made lowercase.
    medication_datetime = models.IntegerField()  # Field name made lowercase.
    medicine_id = models.IntegerField()  # Field name made lowercase.
    medicine_form = models.CharField( max_length=5)  # Field name made lowercase.
    medicine_name = models.CharField( max_length=100)  # Field name made lowercase.
    medicine_duration = models.IntegerField()  # Field name made lowercase.
    medicine_doses = models.IntegerField()  # Field name made lowercase.
    medicine_dose_interval = models.CharField( max_length=15)  # Field name made lowercase.
    medicine_instruction_id = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    medicine_category = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    medicine_extrafield1 = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    medicine_extrafield2 = models.IntegerField( blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deleted_reason = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblpatient_medications'

#######################################TblpatientPayments
class TblpatientPayments(models.Model):
    patient_payment_id = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_status = models.IntegerField()  # Field name made lowercase.
    payment_mode = models.IntegerField()  # Field name made lowercase.
    payment_amount = models.IntegerField()  # Field name made lowercase.
    payment_transaction_no = models.CharField( max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    deleted_reason = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblpatient_payments'

############################################Tblpatientbiometrics
class Tblpatientbiometrics(models.Model):
    patient_biometricid = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    consultation_id = models.ForeignKey(Tblconsultations, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    patient_status = models.IntegerField()  # Field name made lowercase.
    patient_height = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    patient_weight = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    patient_bmi = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblpatientbiometrics'


###########################################Tblpatientvitals
class Tblpatientvitals(models.Model):
    patient_biometricid = models.AutoField( primary_key=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    consultation_id = models.ForeignKey(Tblconsultations, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    patient_status = models.IntegerField()  # Field name made lowercase.
    patient_heartratepluse = models.FloatField()  # Field name made lowercase.
    patient_bpsystolic = models.FloatField()  # Field name made lowercase.
    patient_bpdistolic = models.FloatField()  # Field name made lowercase.
    patient_painscale = models.FloatField()  # Field name made lowercase.
    patient_respiratoryrate = models.FloatField()  # Field name made lowercase.
    patient_temparature = models.FloatField()  # Field name made lowercase.
    patient_chest = models.CharField( max_length=100)  # Field name made lowercase.
    patient_ecg = models.CharField( max_length=100)  # Field name made lowercase.
    createdby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    createdon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField( blank=True, null=True,default="0")  # Field name made lowercase.
    deletedby = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.patient_biometricid

    class Meta:
        db_table = 'tblpatientvitals'



class ConsultationFee(models.Model):
    consultation_fee_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE,null=True,related_name="consultaion_fee_doctor_id")
    location_id = models.ForeignKey(Tbldoctorlocations, on_delete=models.CASCADE,null=True,related_name="consultaion_fee_location_id")
    mode_type = models.IntegerField()
    first_visit_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    second_visit_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'consultation_fee'


class MedicalServicesFee(models.Model):
    medical_service_fee_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE,null=True,related_name="service_fee_doctor_id")
    location_id = models.ForeignKey(Tbldoctorlocations, on_delete=models.CASCADE,null=True,related_name="service_fee_location_id")
    service = models.IntegerField()
    charges = models.IntegerField()
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'medical_services_fee'



class tblChatScripts(models.Model):
    Script_id = models.AutoField(primary_key=True)
    Script_Code = models.IntegerField(null=True, blank=True)
    Location_token = models.ForeignKey(Tbldoctorlocations,on_delete=models.CASCADE,null=True,to_field="location_token")
    Script_Type = models.IntegerField(null=True, blank=True)
    Script_Language = models.CharField( max_length=2, blank=True, null=True) 
    Script_Text = models.TextField(blank=True, null=True)
    S1 = models.IntegerField(null=True, blank=True)
    S2 = models.IntegerField(null=True, blank=True)

    created_on = models.IntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.IntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'tblChatScripts'

class tblScriptOptions(models.Model):
    Script_Option_Id = models.AutoField(primary_key=True)
    Location_token = models.ForeignKey(Tbldoctorlocations,on_delete=models.CASCADE,null=True,to_field="location_token")
    Script_Code = models.ForeignKey(tblChatScripts, on_delete=models.CASCADE,null=True,to_field="Script_id" )
    Script_Option_Type = models.IntegerField(null=True, blank=True)
    Script_Option_Langauge = models.CharField( max_length=2, blank=True, null=True) 
    Script_Option_Text = models.TextField(blank=True, null=True)
    Script_Option_Value = models.CharField( max_length=10, blank=True, null=True) 
    Script_Option_Action_Script_Id = models.IntegerField(null=True, blank=True)

    created_on = models.IntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.IntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'tblScriptOptions'


class tblUserActions(models.Model):
    Action_Id = models.AutoField(primary_key=True)
    Location_token = models.ForeignKey(Tbldoctorlocations,on_delete=models.CASCADE,null=True,to_field="location_token")
    User_Id = models.IntegerField(null=True, blank=True)
    Script_Code = models.ForeignKey(tblChatScripts, on_delete=models.CASCADE,null=True,to_field="Script_id" )
    Script_Option_Id = models.IntegerField(null=True, blank=True)
    Script_Option_Langauge = models.CharField( max_length=2, blank=True, null=True) 
    Script_Action_Input = models.CharField( max_length=100, blank=True, null=True) 
    Script_Option_Value = models.CharField( max_length=100, blank=True, null=True) 

    created_on = models.IntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.IntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)
    class Meta:
        managed = True
        db_table = 'tblUserActions'
