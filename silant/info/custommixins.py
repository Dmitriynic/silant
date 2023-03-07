from django.db.models import Q
from .models import Car, Maintenance, Complaint

class CarListMixin(object,):
    model = Car

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if user.is_superuser or user.groups.filter(name = 'manager').exists() or not user.is_authenticated:
            return
        else:
            return queryset.filter(Q(client__user = user) | Q(service_company__user = user))

class MaintenanceListMixin(object,):
    model = Maintenance

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if user.is_superuser or user.groups.filter(name = 'manager').exists():
            return 
        else:
            return queryset.filter(Q(car__client__user = user) | Q(service_company__user = user))
        
        
class ComplaintListMixin(object,):
    model = Complaint

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if user.is_superuser or user.groups.filter(name = 'manager').exists():
            return 
        else:
            return queryset.filter(Q(car__client__user = user) | Q(service_company__user = user))