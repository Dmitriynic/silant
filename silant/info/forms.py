from django import forms
from .models import (
    Car, Maintenance, Complaint, TechniqueModel, EngineModel, TransmissionModel,
    DriveAxleModel, SteerableBridgeModel, TypeOfMaintenance, NatureOfFailure,
    RecoveryMethod, 
)


class CarForm(forms.ModelForm):
   class Meta:
       model = Car
       fields = [
           'machine_serial_number',
           'technique_model',
           'engine_model',
           'engine_serial_number',
           'transmission_model',
           'transmission_serial_number',
           'drive_axle_model',
           'drive_axle_serial_number',
           'steerable_bridge_model',
           'steerable_bridge_serial_number',
           'supply_contract',
           'date_of_shipment',
           'end_user',
           'delivery_address',
           'equipment',
           'client',
           'service_company',
       ]
    
   def __init__(self, *args, **kwargs):
       user = kwargs.pop('user', None)
       super(CarForm, self).__init__(*args, **kwargs)

       if user and not user.is_authenticated:
           self.fields['supply_contract'].widget.attrs['disabled'] = True
           self.fields['date_of_shipment'].widget.attrs['disabled'] = True
           self.fields['end_user'].widget.attrs['disabled'] = True
           self.fields['delivery_address'].widget.attrs['disabled'] = True
           self.fields['equipment'].widget.attrs['disabled'] = True
           self.fields['client'].widget.attrs['disabled'] = True
           self.fields['service_company'].widget.attrs['disabled'] = True

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = [
           'type',
           'date',
           'operating',
           'orders_number',
           'orders_date',
           'organization',
           'car',
           'service_company',
        ]

class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'orders_date',
            'operating',
            'order_note',
            'order_description',
            'recovery_method',
            'used_spare_parts',
            'recovery_date',
            'downtime',
            'car',
            'service_company',
        ]

class TechniqueModelsForm(forms.ModelForm):
    class Meta:
        model = TechniqueModel
        fields = [
            'title',
            'description',
        ]

class EngineModelsForm(forms.ModelForm):
    class Meta:
        model = EngineModel
        fields = [
            'title',
            'description',
        ]

class TransmissionModelsForm(forms.ModelForm):
    class Meta:
        model = TransmissionModel
        fields = [
            'title',
            'description',
        ]

class DriveAxleModelsForm(forms.ModelForm):
    class Meta:
        model = DriveAxleModel
        fields = [
            'title',
            'description',
        ]

class SteerableBridgeModelsForm(forms.ModelForm):
    class Meta:
        model = SteerableBridgeModel
        fields = [
            'title',
            'description',
        ]

class TypeOfMaintenancesForm(forms.ModelForm):
    class Meta:
        model = TypeOfMaintenance
        fields = [
            'title',
            'description',
        ]

class NatureOfFailuresForm(forms.ModelForm):
    class Meta:
        model = NatureOfFailure
        fields = [
            'title',
            'description',
        ]

class RecoveryMethodsForm(forms.ModelForm):
    class Meta:
        model = EngineModel
        fields = [
            'title',
            'description',
        ]