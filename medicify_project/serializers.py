from rest_framework import serializers
from .models import Tbldoctorappointments, TblmedicineInstructions, Tbldatacodemaster, TblpatientFindingsandsymtoms, TblpatientLabinvestigations, TblpatientMedications,Tblpatientbiometrics,Tblconsultations, Tblprescriptions
from .models import TbldoctorMedicines
from .models import Tbldoctorlocations
from .models import Tbldoctors  # Import the correct model
from .models import Tbldoctorlocationavailability
from .models import TblpateintCharges, TblpatientPayments
from .models import TblpatientPayments
from .models import *


class TbldoctorappointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldoctorappointments
        fields = '__all__'

class TblmedicineInstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblmedicineInstructions
        fields = '__all__'


class DataCodeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldatacodemaster
        fields = '__all__'

class PatientBiometricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpatientbiometrics
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblconsultations
        fields = '__all__'

class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblprescriptions
        fields = '__all__'


class FindingsandsymtomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientFindingsandsymtoms
        fields = '__all__'

class MedicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientMedications
        fields = '__all__'

class LabinvestigationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientLabinvestigations
        fields = '__all__'


######################### Doctor Medicines ############################
class TbldoctorMedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbldoctorMedicines
        fields = '__all__'
        
######################### Doctor Locations ############################        
class DoctorLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldoctorlocations
        fields = '__all__'
        
######################### Doctor ############################         
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldoctors  # Use the correct model
        fields = '__all__'
        
######################### Doctor location Availability ############################    
class DoctorLocationAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldoctorlocationavailability
        fields = '__all__'
        
######################### Patient Charges ############################   
class PatientChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpateintCharges
        fields = '__all__'
        
######################### Patient Payments ############################           
class TblpatientPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientPayments
        fields = '__all__'

######################### Doctor Appointments ############################           
class TbldoctorappointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldoctorappointments
        fields = '__all__'

######################### Appointment ############################   
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldoctorappointments
        fields = ['doctor_id', 'appointment_datetime', 'appointment_name', 'appointment_mobileno', 'appointment_gender']

######################### Patient Vitals ############################   
class TblPatientVitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpatientvitals
        fields = '__all__'

######################### Patients ############################   
class TblpatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpatients
        fields = '__all__'
 
 ######################### Patient Charges ############################      



######################### Patient Payments ############################   
class TblpatientPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientPayments
        fields = ['doctor_id', 'patient_id', 'patient_status', 'payment_mode', 'payment_amount', 'payment_transaction_no','isdeleted']

######################### Patient ############################   
class TblPatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpatients
        fields = [
            'patient_mobileno', 'patient_firstname', 'patient_lastname',
            'patient_fateherhusbandname', 'patient_gender', 'patient_dateofbirth',
            'patient_maritalstatus', 'patient_aadharnumber', 'patient_universalhealthid',
            'patient_bloodgroup', 'patient_level', 'patient_emergencycontact',
            'patient_address', 'patient_cityid', 'patient_stateid', 'patient_countryid',
            'isdeleted','istestpatient',
        ]

######################### Patient Findingsandsymtoms ############################   
class TblpatientFindingsandsymtomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientFindingsandsymtoms
        fields = [
            'patient_id',
            'doctor_id',
            'patient_status',
            'findgings_datetime',
            'consultation_id',
            'findings',
            'symtoms',
            'kco',
            'advice',
            'isdeleted',
        ]

######################### Patient Complaints ############################   
class TblpatientComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientComplaints
        fields = [
            'doctor_id',
            'patient_id',
            'complaint_datetime',
            'complaint_details',
            'appointment_id',
            'consultation_id',
            'isdeleted',
        ]

class LabInvestigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientLabinvestigations
        fields = '__all__'


class ConsultationFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationFee
        fields = '__all__'

class MedicalServicesFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalServicesFee
        fields = '__all__'



class TbllabinvestigationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbllabinvestigations
        fields = '__all__'

class tblChatScriptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblChatScripts
        fields = '__all__'

class tblScriptOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblScriptOptions
        fields = '__all__'

class tblUserActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblUserActions
        fields = '__all__'

        