from django_filters import FilterSet
from .models import Car, Maintenance, Complaint

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class CarsFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Car
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.

        fields = {
           # поиск по названию
            'machine_serial_number' : ['icontains'],
            'technique_model__title': ['icontains'],
            'engine_model__title': ['icontains'],
            'transmission_model__title': ['icontains'],
            'drive_axle_model__title': ['icontains'],
            'steerable_bridge_model__title': ['icontains'],
        }

class MaintenancesFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Maintenance
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.

        fields = {
           # поиск по названию
            'type__title': ['icontains'],
            'car__machine_serial_number': ['icontains'],
            'service_company__title': ['icontains'],
        }

class ComplaintsFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Complaint
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.

        fields = {
           # поиск по названию
            'order_note__title': ['icontains'],
            'recovery_method__title': ['icontains'],
            'service_company__title': ['icontains'],
        }