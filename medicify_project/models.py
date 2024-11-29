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
    basic_education = models.CharField( max_length=255, blank=True, null=True) 
    additional_education = models.CharField( max_length=255, blank=True, null=True) 
    services_offered = models.TextField(blank=True, null=True) 
    password= models.CharField(max_length=32, blank=True, null=True) 

    class Meta:
        db_table = 'tbldoctors'

######################################Tbldatacodemaster
class Tbldatacodemaster(models.Model):
    datacodeid = models.AutoField( primary_key=True)  # Field name made lowercase.
    datacodename = models.CharField( max_length=256)  # Field name made lowercase.
    datacodevalue = models.CharField( max_length=256)  # Field name made lowercase.
    datacodedescription = models.TextField()  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE,null=True,related_name="tbldatacodemaster_doctor_id")

    class Meta:
        db_table = 'tbldatacodemaster'


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
    follower = models.IntegerField(null=True,blank=True)
    outstanding = models.IntegerField(null=True,blank=True)

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
    appointment_id = models.IntegerField( blank=True, null=True) 
    consultation_status=models.IntegerField( blank=True, null=True)
    
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
    medicine_preservation = models.CharField( max_length=256)  # Field name made lowercase.
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
    price = models.IntegerField( blank=True, null=True)

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
    services_offered_at = models.TextField(blank=True, null=True)
    location_image = models.ImageField(upload_to='location_images/', null=True, blank=True)

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
    previous_outstanding = models.IntegerField(blank=True,null=True)
    new_outstanding = models.IntegerField(blank=True,null=True)

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
    labinvestigation_category =  models.CharField( max_length=50, blank=True, null=True) # Field name made lowercase.
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
    medicine_doses = models.TextField(blank=True, null=True)  # Field name made lowercase.
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
    previous_outstanding = models.IntegerField(blank=True,null=True)
    new_outstanding = models.IntegerField(blank=True,null=True)

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
    height = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    appointment_id = models.ForeignKey(Tbldoctorappointments, on_delete=models.SET_NULL, null=True)
    
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
    avg_time_per_patient = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)

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


#############################################
                
class Tbldoctorleave(models.Model):
    doctor_leave_id = models.AutoField(primary_key=True, auto_created=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE,related_name="doctorleave_doctor_id")  # Foreign key to Tbldoctors
    location_id = models.ForeignKey(Tbldoctorlocations, on_delete=models.CASCADE,related_name="doctorleave_location_id")  # Foreign key to Tbldoctorlocations
    day = models.IntegerField()  # Field for day (int)
    leave_date = models.BigIntegerField()  # Field for leave date (BigInt)
    order = models.IntegerField()  # Field for order (int) order means 1-morning 2-afternoon and 3-evening
    updated_date = models.BigIntegerField()  # Field for updated on (BigInt)
    start_time = models.IntegerField()  # Field for start time (int)
    end_time = models.IntegerField()  # Field for end time (int)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'tbldoctorleave'

class tblUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    location_id = models.ForeignKey(Tbldoctorlocations, on_delete=models.CASCADE, null=True, related_name="user_location_id")
    user_name = models.CharField(max_length=100)
    user_mobileno = models.CharField(max_length=10)
    user_login_token = models.CharField(max_length=32,blank=True,null=True,unique=True)
    user_role = models.IntegerField(null=True,blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tblUsers'



class tblMasterDisease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=100)
    disease_type = models.IntegerField(null=True,blank=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="masterdisease_doctor_id")
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tblMasterDisease'

class tblPatientDisease(models.Model):
    patient_disease_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Tblpatients,on_delete=models.CASCADE, null=True, related_name="patientdisease_patient_id")
    disease_id = models.ForeignKey(tblMasterDisease,on_delete=models.CASCADE, null=True, related_name="patientdisease_disease_id")
    disease_entry_date = models.BigIntegerField()
    disease_details = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tblPatientDisease'

class tblMasterAllergies(models.Model):
    allergy_id = models.AutoField(primary_key=True)
    allergy_name = models.CharField(max_length=100)
    allergy_type = models.IntegerField(null=True,blank=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="masterallergy_doctor_id")
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0) 

    class Meta:
        db_table = 'tblMasterAllergies'


class tblPatientAllergies(models.Model):
    patient_allergy_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Tblpatients,on_delete=models.CASCADE, null=True, related_name="patientallergy_patient_id")
    allergy_id = models.ForeignKey(tblMasterAllergies,on_delete=models.CASCADE, null=True, related_name="patientallergy_disease_id")
    allergy_entry_date = models.BigIntegerField()
    allergy_details = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tblPatientAllergies'


class tblPatientDoctorLink(models.Model):
    patientdoctorlink_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="patientdoctorlink_doctor_id")
    patient_id = models.ForeignKey(Tblpatients,on_delete=models.CASCADE, null=True, related_name="patientdoctorlink_patient_id")
    link_approval = models.CharField(max_length=10, default='yes')
    link_reject_reason = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)
    remark = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'tblPatientDoctorLink'


class PrescriptionSettings(models.Model):
    prescriptionsettings_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="prescription_doctor_id")
    location_id = models.ForeignKey(Tbldoctorlocations, on_delete=models.CASCADE, null=True, related_name="prescription_location_id")
    paper_size = models.IntegerField(null=True, blank=True)
    clinic_logo_alignment = models.IntegerField(null=True, blank=True)
    header_type = models.IntegerField(null=True, blank=True)
    header_image = models.ImageField(upload_to='header_images/', null=True, blank=True)
    header_top_margin = models.FloatField(null=True, blank=True)
    clinic_name = models.IntegerField(default=0)
    clinic_address = models.IntegerField(default=0)
    doctor_name = models.IntegerField(default=0)
    doctor_degree = models.IntegerField(default=0)
    doctor_speciality = models.IntegerField(default=0)
    doctor_availability = models.IntegerField(default=0)
    clinic_services = models.IntegerField(default=0)
    clinic_logo = models.IntegerField(default=0)
    clinic_mobile_number = models.IntegerField(default=0)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'prescription_settings'


class TblLead(models.Model):
    lead_id = models.AutoField(primary_key=True)
    franchise_id = models.IntegerField(default=0, null=True, blank=True)
    lead_name = models.CharField(max_length=100, null=True, blank=True)
    lead_email = models.CharField(max_length=50, null=True, blank=True)
    lead_dob =  models.BigIntegerField(null=True, blank=True)
    lead_contact_no = models.CharField(max_length=15, null=True, blank=True)
    lead_source = models.IntegerField(null=True, blank=True)
    lead_sub_source = models.TextField(null=True, blank=True)
    lead_product = models.CharField(max_length=50, default="1", null=True, blank=True)
    lead_status = models.IntegerField(default=1, null=True, blank=True)
    lead_date_time_stamp = models.BigIntegerField(null=True, blank=True)
    lead_by_id = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0, null=True, blank=True)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    lead_department = models.IntegerField(null=True, blank=True)
    crm_ref_id = models.IntegerField(default=0, null=True, blank=True)
    lead_stage = models.IntegerField(default=1, null=True, blank=True)
    lead_country =  models.IntegerField(null=True, blank=True)
    lead_state =  models.IntegerField(null=True, blank=True)
    lead_city =  models.IntegerField(null=True, blank=True)
    lead_handler_id = models.IntegerField(null=True, blank=True)
    lead_handler_type = models.SmallIntegerField(default=1, null=True, blank=True)
    lead_followup_old_status = models.SmallIntegerField(default=0, null=True, blank=True)
    lead_month_year = models.CharField(max_length=50, null=True, blank=True)
    app_id =  models.IntegerField(default=2, null=True, blank=True)
    lead_added_on = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'tblLeads'


class TblLeadFollowUp(models.Model):
    follow_up_id = models.AutoField(primary_key=True)
    lead_id = models.ForeignKey(TblLead, on_delete=models.CASCADE, null=True, related_name="LeadFollowUp_lead_id")
    follow_up_date_time_stamp = models.BigIntegerField(null=True, blank=True)
    follow_up_method = models.IntegerField(null=True, blank=True)
    follow_up_details = models.TextField(null=True, blank=True)
    follow_up_success_status = models.IntegerField(null=True, blank=True)
    follow_up_activity = models.IntegerField(default=0, null=True, blank=True)
    next_follow_up_date_time_stamp = models.BigIntegerField(null=True, blank=True)
    next_follow_up_method = models.IntegerField(null=True, blank=True)
    next_follow_up_action = models.TextField(null=True, blank=True)
    follow_up_by = models.IntegerField(null=True, blank=True)
    follow_up_user_id = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0, null=True, blank=True)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    by_department = models.IntegerField(default=0, null=True, blank=True)
    app_id = models.IntegerField(default=2, null=True, blank=True)

    class Meta:
        db_table = 'tblLeadFollowUp'


class TblCountries(models.Model):
    id = models.AutoField(primary_key=True)
    sortname = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phonecode = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'tblCountries'


class TblStates(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(TblCountries, on_delete=models.CASCADE, null=True, blank=True, related_name='states')

    class Meta:
        db_table = 'tblStates'


class TblCities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey(TblStates, on_delete=models.CASCADE, null=True, blank=True, related_name='cities')

    class Meta:
        db_table = 'tblCities'



##############################Subscriptions Model
class TblMasterSubscription(models.Model):
    master_subscription_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tax_one = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tax_two = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_trial = models.BooleanField(null=True, blank=True)
    total_days = models.IntegerField(null=True, blank=True)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tblmaster_subscription'

class TblDoctorSubscription(models.Model):
    doctor_subscription_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="subscription_doctor_id")
    master_subscription_id = models.ForeignKey(TblMasterSubscription, on_delete=models.CASCADE, null=True, related_name="doctorsubscription_mastersubscription_id")
    subscription_start_on = models.BigIntegerField(null=True, blank=True)
    subscription_end_on = models.BigIntegerField(null=True, blank=True)
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_tax1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_tax2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_paid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_discount_type = models.IntegerField(null=True, blank=True)
    subscription_promo_code = models.CharField(max_length=50, null=True, blank=True)
    subscription_type = models.IntegerField(null=True, blank=True)
    subscription_billing_name = models.CharField(max_length=100, null=True, blank=True)
    subscription_billing_GstNo = models.CharField(max_length=50, null=True, blank=True)
    subscription_billing_address = models.CharField(max_length=255, null=True, blank=True)
    subscription_billing_pincode = models.CharField(max_length=20, null=True, blank=True)
    subscription_billing_city = models.IntegerField(null=True, blank=True)
    subscription_status = models.IntegerField(default=0,null=True,blank=True) #status 0 Active and status 1 unactive.
    entry_operator_type = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tbldoctor_subscription'


class TblDoctorSubscriptionPromocodes(models.Model):
    promocode_id = models.AutoField(primary_key=True)
    promo_code = models.CharField(max_length=100, null=True, blank=True)
    promo_code_activation_on = models.BigIntegerField(null=True, blank=True)
    promo_code_valid_till = models.BigIntegerField(null=True, blank=True)
    promo_code_value = models.IntegerField(null=True, blank=True)
    promo_code_value_type = models.IntegerField(null=True, blank=True)
    promo_code_status = models.IntegerField(null=True, blank=True)
    entry_operator_id = models.CharField(max_length=100, null=True, blank=True)
    entry_operator_type = models.CharField(max_length=100, null=True, blank=True)
    promo_code_used_by = models.CharField(max_length=100, null=True, blank=True)
    promo_code_used_on = models.BigIntegerField(null=True, blank=True)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tbl_doctor_subscription_promocodes'




######################################################### FCM ###########################
class CustomFCMDevice(models.Model):
    device_id = models.AutoField(primary_key=True)
    app_id = models.IntegerField(null=True, blank=True, default=0)
    userId= models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True, related_name='fcm_devices')
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    version = models.CharField(max_length=250, null=True, blank=True)
    browser = models.CharField(max_length=250, null=True, blank=True)
    registration_id = models.CharField(max_length=255, null=True, blank=True)
    # Add other custom fields here if needed

    def _str_(self):
        return str(self.device_id)

    class Meta:
        db_table = "CustomFCMDevice"
        
        
        
        
class NotificationCRM(models.Model):
    notification_id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True, related_name='admin_collection_notification')
    fcm_token = models.CharField(max_length=255, null=True, blank=True)
    notification_icon = models.FileField(blank=True, null=True, upload_to='notification/admin_collection_notification_icon/', max_length=2000)
    notification_image = models.FileField(blank=True, null=True, upload_to='notification/admin_collection_notification_image/', max_length=2000)
    notification_title = models.CharField(max_length=255, null=True, blank=True)
    notification_body = models.TextField(null=True, blank=True)
    notification_action = models.CharField(max_length=255, null=True, blank=True)
    notification_send = models.DateTimeField(null=True)
    notification_delivered = models.DateTimeField(null=True)
    notification_read = models.DateTimeField(null=True)
    notification_status = models.CharField(max_length=255, null=True, blank=True)
    notification_category = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True, related_name='admin_collection_notifications_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True, related_name='admin_collection_notifications_last_modified_by')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True, related_name='admin_collection_notifications_deleted_by')
    delete_reason = models.CharField(max_length=150, null=True, blank=True)

    def _str_(self):
        return str(self.notification_id)
    
    class Meta:
        db_table = "NotificationCRM"


class tblPharmacist(models.Model):
    pharmacist_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=100,null=True,blank=True)
    shop_address = models.CharField(max_length=255,null=True,blank=True)
    shop_contact_number = models.CharField(max_length=15,null=True,blank=True)
    shop_owner_name = models.CharField(max_length=100,null=True,blank=True)
    shop_owner_number = models.CharField(max_length=15,null=True,blank=True)
    pharmacist_username = models.CharField(max_length=50,null=True,blank=True)
    pharmacist_password = models.CharField(max_length=128,null=True,blank=True)
    pharmacist_token = models.CharField(max_length=32, blank=True, null=True)
    pharmacist_type = models.IntegerField(null=True,blank=True)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = "tblPharmacist"


class tblDoctorPharmacistlink(models.Model):
    doctorpharmacist_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="doctorpharmacist_doctor_id")
    location_id = models.ForeignKey(Tbldoctorlocations, on_delete=models.CASCADE, null=True, related_name="doctorpharmacist_location_id")
    pharmacist_id = models.ForeignKey(tblPharmacist, on_delete=models.CASCADE, null=True, related_name="doctorpharmacist_pharmacist_id")
    status = models.IntegerField(default=0) # 0 means active or currently assosciated.
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = "tblDoctorPharmacistlink"


class tblPrescribePharmacist(models.Model):
    prescribepharmacist_id = models.AutoField(primary_key=True)
    prescription_id = models.ForeignKey(Tblprescriptions, on_delete=models.CASCADE, null=True, related_name="prescriptionpharmacist_prescription_id")
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="prescriptionpharmacist_doctor_id")
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.CASCADE, null=True, related_name="prescriptionpharmacist_patient_id")
    pharmacist_id = models.ForeignKey(tblPharmacist, on_delete=models.CASCADE, null=True, related_name="prescriptionpharmacist_pharmacist_id")
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)
    pharma_status = models.IntegerField(default=0)

    class Meta:
        db_table = "tblPrescribePharmacist"



class tblLaboratory(models.Model):
    laboratory_id = models.AutoField(primary_key=True)
    laboratory_name = models.CharField(max_length=100,null=True,blank=True)
    laboratory_address = models.CharField(max_length=255,null=True,blank=True)
    laboratory_contact_number = models.CharField(max_length=15,null=True,blank=True)
    laboratory_owner_name = models.CharField(max_length=100,null=True,blank=True)
    laboratory_owner_number = models.CharField(max_length=15,null=True,blank=True)
    laboratory_username = models.CharField(max_length=50,null=True,blank=True)
    laboratory_password = models.CharField(max_length=128,null=True,blank=True)
    laboratory_token = models.CharField(max_length=32, blank=True, null=True)
    laboratory_type = models.IntegerField(null=True,blank=True)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = "tblLaboratory"


class tblDoctorLaboratorylink(models.Model):
    doctorlaboratory_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="doctorlaboratory_doctor_id")
    location_id = models.ForeignKey(Tbldoctorlocations, on_delete=models.CASCADE, null=True, related_name="doctorlaboratory_location_id")
    laboratory_id = models.ForeignKey(tblLaboratory, on_delete=models.CASCADE, null=True, related_name="doctorlaboratory_laboratory_id")
    status = models.IntegerField(default=0) # 0 means active or currently assosciated.
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = "tblDoctorLaboratorylink"


class tblPrescribeLaboratory(models.Model):
    prescribelaboratory_id = models.AutoField(primary_key=True)
    prescription_id = models.ForeignKey(Tblprescriptions, on_delete=models.CASCADE, null=True, related_name="prescriptionlaboratory_prescription_id")
    doctor_id = models.ForeignKey(Tbldoctors, on_delete=models.CASCADE, null=True, related_name="prescriptionlaboratory_doctor_id")
    patient_id = models.ForeignKey(Tblpatients, on_delete=models.CASCADE, null=True, related_name="prescriptionlaboratory_patient_id")
    laboratory_id = models.ForeignKey(tblLaboratory, on_delete=models.CASCADE, null=True, related_name="prescriptionlaboratory_laboratory_id")
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)
    laboratory_status = models.IntegerField(default=0)

    class Meta:
        db_table = "tblPrescribeLaboratory"


################################Deal related Models##########################

class tblDealsCategories(models.Model):
    DealCategory_id = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255,null=True,blank=True)
    CategoryMedicalNonMedical = models.IntegerField(null=True,blank=True)
    CategoryKewords = models.TextField(null=True,blank=True)
    CategoryStatus = models.IntegerField(default=1)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = "tblDealsCategories"


class tblDeals(models.Model):
    Deal_id = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255,null=True,blank=True)
    DealOwnerMobileNo = models.CharField(max_length=15,null=True,blank=True)
    DealOwnerPersonName = models.CharField(max_length=255,null=True,blank=True)
    DealMedicalNonMedical = models.IntegerField(default=1)
    DealCategory_id = models.ForeignKey(tblDealsCategories, on_delete=models.CASCADE, null=True, related_name="tblDeal_DealCategory_id")
    DealTitle = models.CharField(max_length=255,null=True,blank=True)
    DealKeywords = models.TextField(null=True,blank=True)
    DealContentType = models.IntegerField(default=1)
    DealContentURL_forWeb = models.CharField(max_length=255,null=True,blank=True)
    DealContentURL_forMobile = models.CharField(max_length=255,null=True,blank=True)
    DealWebsiteURL = models.CharField(max_length=255,null=True,blank=True)
    Show_to_Doctor = models.IntegerField(default=1) # 1=yes ,0=no
    Show_to_Pharmacy = models.IntegerField(default=1)
    Show_to_Labs = models.IntegerField(default=1)
    DealStatus = models.IntegerField(default=1)
    DealViews = models.IntegerField(default=0)
    DealLikes = models.IntegerField(default=0)
    DealInterests = models.IntegerField(default=0)
    DealClicks = models.IntegerField(default=0)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tblDeals'


class tblDealPublish(models.Model):
    DealPublish_id = models.AutoField(primary_key=True)
    Deal_id = models.ForeignKey(tblDeals, on_delete=models.CASCADE, null=True, related_name="tblDealPublish_Deal_id")
    PublishedOn = models.BigIntegerField(null=True,blank=True)
    ExpiryOn = models.BigIntegerField(null=True,blank=True)
    PaymentDetails = models.CharField(max_length=255,null=True,blank=True)
    DealStatus = models.IntegerField(default=1)
    DeleteReason = models.CharField(max_length=255,null=True,blank=True)
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tblDealPublish'


class tblDealActionRecorder(models.Model):
    DealAction_id = models.AutoField(primary_key=True)
    DealActionType = models.IntegerField()  #'0':View 
    DealActionDateTime = models.BigIntegerField(null=True,blank=True)
    DealPublish_id = models.ForeignKey(tblDealPublish, on_delete=models.CASCADE, null=True, related_name="tblDealActionRecorder_DealPublish_id")
    DealActionUser_id = models.IntegerField(null=True,blank=True) # User id  will be doctorid or pharma id or laboratory id depending which user seen the deal.
    DealActionUser_type = models.IntegerField(null=True,blank=True) #User_type means doctor or pharma or laboratory
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)
    DealLike = models.IntegerField(default=0 ,null=True,blank=True)
    DealInterest = models.IntegerField(default=0,null=True,blank=True)
    DealShare = models.IntegerField(default=0,null=True,blank=True)

    class Meta:
        db_table = 'tblDealActionRecorder'

class tblDealCategoryLink(models.Model):
    DealCategorylink_id = models.AutoField(primary_key=True)
    DealCategory_id = models.ForeignKey(tblDealsCategories, on_delete=models.CASCADE, null=True, related_name="tblDealCategoryLink_DealCategory_id")
    DealPublish_id = models.ForeignKey(tblDealPublish, on_delete=models.CASCADE, null=True, related_name="tblDealCategoryLink_DealPublish_id")
    Deal_id = models.ForeignKey(tblDeals, on_delete=models.CASCADE, null=True, related_name="tblDealCategoryLink_Deal_id")
    created_on = models.BigIntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.BigIntegerField(null=True, blank=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'tblDealCategoryLink'








