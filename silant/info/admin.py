from django.contrib import admin
from .models import TechniqueModel, EngineModel, TransmissionModel, DriveAxleModel, SteerableBridgeModel, TypeOfMaintenance, NatureOfFailure, RecoveryMethod, Service_Company, Client, Car, Maintenance, Complaint

# Register your models here.

admin.site.register(TechniqueModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteerableBridgeModel)
admin.site.register(TypeOfMaintenance)
admin.site.register(NatureOfFailure)
admin.site.register(RecoveryMethod)
admin.site.register(Service_Company)
admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Maintenance)
admin.site.register(Complaint)