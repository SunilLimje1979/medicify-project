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
        fields = '__all__'

######################### Patient ############################   
class TblPatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpatients
        fields = '__all__'

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
            'patient_findings_id',
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


##########################Doctor Leave########################
class TbldoctorleaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbldoctorleave
        fields = '__all__'

class PatientMedicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblpatientMedications
        fields = '__all__'

class TblPrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblprescriptions
        fields = '__all__'

class TblUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblUsers
        fields = '__all__'


class TblMasterDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblMasterDisease
        fields = '__all__'


class TblPatientDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblPatientDisease
        fields = '__all__'
    

class TblMasterAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = tblMasterAllergies
        fields = '__all__'


class TblPatientAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = tblPatientAllergies
        fields = '__all__'

class TblPatientDoctorLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblPatientDoctorLink
        fields = '__all__'
        

class PrescriptionSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionSettings
        fields = '__all__'  # Serialize all fields

class TblLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblLead
        fields = '__all__'  # Serialize all fields

class TblLeadFollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblLeadFollowUp
        fields = '__all__'  # Serialize all fields



############################Serializers for Countries,States,Cities

# Simple Serializers
class TblCountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCountries
        fields = '__all__'

class TblStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblStates
        fields = '__all__'

class TblCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCities
        fields = '__all__'

# Nested Serializers
class NestedTblStatesSerializer(serializers.ModelSerializer):
    country = TblCountriesSerializer()

    class Meta:
        model = TblStates
        fields = '__all__'

class NestedTblCitiesSerializer(serializers.ModelSerializer):
    state = NestedTblStatesSerializer()

    class Meta:
        model = TblCities
        fields = '__all__'




###############################Subscriptions Models Serializer
class TblMasterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMasterSubscription
        fields = '__all__'

class TblDoctorSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDoctorSubscription
        fields = '__all__'

class TblDoctorSubscriptionPromocodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDoctorSubscriptionPromocodes
        fields = '__all__'



##########################Notifications

class NotificationCRMSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationCRM
        fields = '__all__'
        

class CustomFCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFCMDevice
        fields = '__all__'


    def validate(self, data):
        user_id = data.get('userId')
        registration_id = data.get('registration_id')
        app_id=data.get('app_id')
        
        if CustomFCMDevice.objects.filter(userId=user_id, registration_id=registration_id,app_id=app_id).exists():
            raise serializers.ValidationError("This user and token combination already exists.")
        
        return data


##################Pharmacist
class tblPharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblPharmacist
        fields = '__all__'

class tblDoctorPharmacistlinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblDoctorPharmacistlink
        fields = '__all__'

class tblPrescribePharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblPrescribePharmacist
        fields = '__all__'
        
    

##################Laboratory
class tblLaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = tblLaboratory
        fields = '__all__'

class tblDoctorLaboratorylinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblDoctorLaboratorylink
        fields = '__all__'

class tblPrescribeLaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = tblPrescribeLaboratory
        fields = '__all__'


#####################For Deal Module

# Serializer for tblDealsCategories
class TblDealsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblDealsCategories
        fields = '__all__'

# Serializer for tblDeals
class TblDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblDeals
        fields = '__all__'

# Serializer for tblDealPublish
class TblDealPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblDealPublish
        fields = '__all__'

# Serializer for tblDealActionRecorder
class TblDealActionRecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblDealActionRecorder
        fields = '__all__'


# Serializer for tblDealCategoryLink
class TblDealCategoryLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblDealCategoryLink
        fields = '__all__'