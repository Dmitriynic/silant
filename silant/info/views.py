from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    Car, Maintenance, Complaint, TechniqueModel, EngineModel, 
    TransmissionModel, DriveAxleModel, SteerableBridgeModel,
    TypeOfMaintenance, NatureOfFailure, RecoveryMethod,
    Service_Company, Client,
)
from .filters import CarsFilter, MaintenancesFilter, ComplaintsFilter
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from .forms import (
    CarForm, MaintenanceForm, ComplaintsForm, TechniqueModelsForm,
    EngineModelsForm, TransmissionModelsForm, DriveAxleModelsForm,
    SteerableBridgeModelsForm, TypeOfMaintenancesForm, NatureOfFailuresForm,
    RecoveryMethodsForm,
)
from django.urls import reverse_lazy
from .custommixins import CarListMixin, MaintenanceListMixin, ComplaintListMixin

# Create your views here.
class CarsList(CarListMixin, ListView):
    #указываем модель, объекты которой мы будем выводить
    model = Car
    form_class = CarForm
    #поле, которое будет использоваться для сортировки объектов
    ordering = '-date_of_shipment'
    #указываем имя шаблона, в котором будут все инструкции о том
    #как именно пользователю должны быть показаны наши объекты
    template_name = 'info/cars.html'
    #это имя списка, в котором будут лежать все объекты.
    #его надо указать, чтобы обратиться к списку объекту в html-шаблоне.
    context_object_name = 'cars'


    # Переопределяем функцию получения списка машин
    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = CarsFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список машин
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       user_in_group_service_complany = self.request.user.groups.filter(name='service_company').exists()
       context['user_in_group_manager'] = user_in_group_manager
       context['user_in_group_service_company'] = user_in_group_service_complany
       return context

class CarDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    #Модель все та же, но мы хотим получать информацию по отдельному товару
    model = Car
    #Используем другой шаблон - car.html
    template_name = 'info/car.html'
    #Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'car'
    permission_required = ('info.view_car', )

    def test_func(self):
       obj = self.get_object()
       ruser = self.request.user
       return obj.client.user == ruser or obj.service_company.user == ruser or ruser.is_superuser or ruser.groups.filter(name='manager').exists()
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context

class CarCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = CarForm
   #модель машин
   model = Car
   # и новый шаблон, в котором используется форма
   template_name = 'info/car_edit.html'
   permission_required = 'info.add_car'

class CarUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   form_class = CarForm
   model = Car
   template_name = 'info/car_edit.html'
   permission_required = 'info.change_car'

class CarDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   model = Car
   template_name = 'info/car_delete.html'
   success_url = reverse_lazy('car_list')
   permission_required = 'info.delete_car'

class MaintenancesList(LoginRequiredMixin, MaintenanceListMixin, ListView):
    model = Maintenance
    #template_name = 'info/maintenances.html'
    template_name = 'info/cars.html'
    context_object_name = 'maintenances'
    permission_required = 'info.view_maintenance'


    # Переопределяем функцию получения списка машин
    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = MaintenancesFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список машин
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       context['ordering'] = self.ordering
       return context

class MaintenanceDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    #Модель все та же, но мы хотим получать информацию по отдельному товару
    model = Maintenance
    #Используем другой шаблон - car.html
    template_name = 'info/maintenance.html'
    #Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'maintenance'
    permission_required = 'info.view_maintenance'
    
    def test_func(self):
       obj = self.get_object()
       ruser = self.request.user
       return obj.car.client.user == ruser or obj.service_company.user == ruser or ruser.is_superuser or ruser.groups.filter(name='manager').exists()

class MaintenanceCreate(LoginRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = MaintenanceForm
   #модель машин
   model = Maintenance
   # и новый шаблон, в котором используется форма
   template_name = 'info/maintenance_edit.html'
   permission_required = 'info.add_maintenance'

class MaintenanceUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   form_class = MaintenanceForm
   model = Maintenance
   template_name = 'info/maintenance_edit.html'
   permission_required = 'info.change_maintenance'

   def test_func(self):
       obj = self.get_object()
       ruser = self.request.user
       return obj.car.client.user == ruser or obj.service_company.user == ruser or ruser.is_superuser or ruser.groups.filter(name='manager').exists()

class MaintenanceDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Maintenance
   template_name = 'info/maintenance_delete.html'
   success_url = reverse_lazy('maintenance_list')
   permission_required = 'info.delete_maintenance'

   def test_func(self):
       obj = self.get_object()
       ruser = self.request.user
       return obj.car.client.user == ruser or obj.service_company.user == ruser or ruser.is_superuser or ruser.groups.filter(name='manager').exists()

class ComplaintsList(LoginRequiredMixin, ComplaintListMixin, ListView):
    model = Complaint
    template_name = 'info/cars.html'
    context_object_name = 'complaints'
    permission_required = 'info.view_complaint'


    # Переопределяем функцию получения списка машин
    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = ComplaintsFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список машин
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context
    
class ComplaintDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    #Модель все та же, но мы хотим получать информацию по отдельному товару
    model = Complaint
    #Используем другой шаблон - car.html
    template_name = 'info/complaint.html'
    #Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'complaint'
    permission_required = 'info.view_complaint'

    def test_func(self):
       obj = self.get_object()
       ruser = self.request.user
       return obj.car.client.user == ruser or obj.service_company.user == ruser or ruser.is_superuser or ruser.groups.filter(name='manager').exists()

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       user_in_group_service_company = self.request.user.groups.filter(name='service_company').exists()
       context['user_in_group_service_company'] = user_in_group_service_company
       return context

class ComplaintCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = ComplaintsForm
   #модель машин
   model = Complaint
   # и новый шаблон, в котором используется форма
   template_name = 'info/complaint_edit.html'
   permission_required = 'info.add_complaint'

class ComplaintUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   form_class = ComplaintsForm
   model = Complaint
   template_name = 'info/complaint_edit.html'
   permission_required = 'info.change_complaint'

   def test_func(self):
       obj = self.get_object()
       ruser = self.request.user
       return obj.service_company.user == ruser or ruser.is_superuser or ruser.groups.filter(name='manager').exists()

class ComplaintDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Complaint
   template_name = 'info/complaint_delete.html'
   success_url = reverse_lazy('complaint_list')
   permission_required = 'info.delete_complaint'

   def test_func(self):
       obj = self.get_object()
       ruser = self.request.user
       return obj.service_company.user == ruser or ruser.is_superuser or ruser.groups.filter(name='manager').exists()

class TechniqueModelDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = TechniqueModel
   template_name = 'info/technique_model.html'
   context_object_name = 'technique_model'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         cars = Car.objects.all()
         for car in cars:
            technique_model = car.technique_model
            if(self.get_object() == technique_model and (car.client.user == ruser or car.service_company.user == ruser)):
               return True
         return False
      
   
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context
      
class TechniqueModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = TechniqueModelsForm
   #модель машин
   model = TechniqueModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/technique_model_edit.html'
   permission_required = 'info.add_techniquemodel'

class TechniqueModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = TechniqueModelsForm
   #модель машин
   model = TechniqueModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/technique_model_edit.html'
   permission_required = 'info.change_techniquemodel'

class TechniqueModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   #указываем разработанную форму
   form_class = TechniqueModelsForm
   #модель машин
   model = TechniqueModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/technique_model_delete.html'
   permission_required = 'info.delete_techniquemodel'
   
class EngineModelDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = EngineModel
   template_name = 'info/engine_model.html'
   context_object_name = 'engine_model'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         cars = Car.objects.all()
         for car in cars:
            engine_model = car.engine_model
            if(self.get_object() == engine_model and (car.client.user == ruser or car.service_company.user == ruser)):
               return True
         return False
      
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context
      
class EngineModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = EngineModelsForm
   #модель машин
   model = EngineModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/engine_model_edit.html'
   permission_required = 'info.add_enginemodel'

class EngineModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = EngineModelsForm
   #модель машин
   model = EngineModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/engine_model_edit.html'
   permission_required = 'info.change_enginemodel'

class EngineModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   #указываем разработанную форму
   form_class = EngineModelsForm
   #модель машин
   model = EngineModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/engine_model_delete.html'
   permission_required = 'info.delete_enginemodel'
      
class TransmissionModelDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = TransmissionModel
   template_name = 'info/transmission_model.html'
   context_object_name = 'transmission_model'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         cars = Car.objects.all()
         for car in cars:
            transmission_model = car.transmission_model
            if(self.get_object() == transmission_model and (car.client.user == ruser or car.service_company.user == ruser)):
               return True
         return False
      
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context
      
class TransmissionModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = TransmissionModelsForm
   #модель машин
   model = TransmissionModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/transmission_model_edit.html'
   permission_required = 'info.add_transmissionmodel'

class TransmissionModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = TransmissionModelsForm
   #модель машин
   model = TransmissionModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/transmission_model_edit.html'
   permission_required = 'info.change_transmissionmodel'

class TransmissionModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   #указываем разработанную форму
   form_class = TransmissionModelsForm
   #модель машин
   model = TransmissionModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/transmission_model_delete.html'
   permission_required = 'info.delete_transmissionmodel'
      
class DriveAxleModelDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = DriveAxleModel
   template_name = 'info/drive_axle_model.html'
   context_object_name = 'drive_axle_model'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         cars = Car.objects.all()
         for car in cars:
            drive_axle_model = car.drive_axle_model
            if(self.get_object() == drive_axle_model and (car.client.user == ruser or car.service_company.user == ruser)):
               return True
         return False
      
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context
      
class DriveAxleModelCreate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = DriveAxleModelsForm
   #модель машин
   model = DriveAxleModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/drive_axle_model_edit.html'
   permission_required = 'info.add_driveaxlemodel'

class DriveAxleModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = DriveAxleModelsForm
   #модель машин
   model = DriveAxleModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/drive_axle_model_edit.html'
   permission_required = 'info.change_driveaxlemodel'
      
class DriveAxleModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   #указываем разработанную форму
   form_class = DriveAxleModelsForm
   #модель машин
   model = DriveAxleModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/drive_axle_model_delete.html'
   permission_required = 'info.delete_driveaxlemodel'

class SteerableBridgeModelDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = SteerableBridgeModel
   template_name = 'info/steerable_bridge_model.html'
   context_object_name = 'steerable_bridge_model'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         cars = Car.objects.all()
         for car in cars:
            steerable_bridge_model = car.steerable_bridge_model
            if(self.get_object() == steerable_bridge_model and (car.client.user == ruser or car.service_company.user == ruser)):
               return True
         return False
      
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context
      
class SteerableBridgeModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = SteerableBridgeModelsForm
   #модель машин
   model = SteerableBridgeModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/steerable_bridge_model_edit.html'
   permission_required = 'info.add_steerablebridgemodel'

class SteerableBridgeModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = SteerableBridgeModelsForm
   #модель машин
   model = SteerableBridgeModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/steerable_bridge_model_edit.html'
   permission_required = 'info.change_steerablebridgemodel'

class SteerableBridgeModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   #указываем разработанную форму
   form_class = SteerableBridgeModelsForm
   #модель машин
   model = SteerableBridgeModel
   # и новый шаблон, в котором используется форма
   template_name = 'info/steerable_bridge_model_delete.html'
   permission_required = 'info.delete_steerablebridgemodel'
      
class TypeOfMaintenanceDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = TypeOfMaintenance
   template_name = 'info/type_of_maintenance.html'
   context_object_name = 'type_of_maintenance'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         maintenances = Maintenance.objects.all()
         for maintenance in maintenances:
            type_of_maintenance = maintenance.type_of_maintenance
            if(self.get_object() == type_of_maintenance and (maintenance.car.client.user == ruser or maintenance.service_company.user == ruser)):
               return True
         return False
      
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context
      
class TypeOfMaintenanceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = TypeOfMaintenancesForm
   #модель машин
   model = TypeOfMaintenance
   # и новый шаблон, в котором используется форма
   template_name = 'info/type_of_maintenance_edit.html'
   permission_required = 'info.add_typeofmaintenance'

class TypeOfMaintenanceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = TypeOfMaintenancesForm
   #модель машин
   model = TypeOfMaintenance
   # и новый шаблон, в котором используется форма
   template_name = 'info/type_of_maintenance_edit.html'
   permission_required = 'info.change_typeofmaintenance'

class TypeOfMaintenanceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   #указываем разработанную форму
   form_class = TypeOfMaintenancesForm
   #модель машин
   model = TypeOfMaintenance
   # и новый шаблон, в котором используется форма
   template_name = 'info/type_of_maintenance_delete.html'
   permission_required = 'info.delete_typeofmaintenance'
      
class NatureOfFailureDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = NatureOfFailure
   template_name = 'info/nature_of_failure.html'
   context_object_name = 'nature_of_failure'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         complaints = Complaint.objects.all()
         for complaint in complaints:
            nature_of_failure = complaint.order_note
            if(self.get_object() == nature_of_failure and (complaint.car.client.user == ruser or complaint.service_company.user == ruser)):
               return True
         return False
      
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context
      
class NatureOfFailureCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = NatureOfFailuresForm
   #модель машин
   model = NatureOfFailure
   # и новый шаблон, в котором используется форма
   template_name = 'info/nature_of_failure_edit.html'
   permission_required = 'info.add_natureoffailure'

class NatureOfFailureUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = NatureOfFailuresForm
   #модель машин
   model = NatureOfFailure
   # и новый шаблон, в котором используется форма
   template_name = 'info/nature_of_failure_edit.html'
   permission_required = 'info.change_natureoffailure'

class NatureOfFailureDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   #указываем разработанную форму
   form_class = NatureOfFailuresForm
   #модель машин
   model = NatureOfFailure
   # и новый шаблон, в котором используется форма
   template_name = 'info/nature_of_failure_delete.html'
   permission_required = 'info.delete_natureoffailure'
      
class RecoveryMethodDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = RecoveryMethod
   template_name = 'info/recovery_method.html'
   context_object_name = 'recovery_method'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         complaints = Complaint.objects.all()
         for complaint in complaints:
            recovery_method = complaint.recovery_method
            if(self.get_object() == recovery_method and (complaint.car.client.user == ruser or complaint.service_company.user == ruser)):
               return True
         return False
      
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #проверяем принадлежность пользователя к группе для отображения кнопки создания машины
       user_in_group_manager = self.request.user.groups.filter(name='manager').exists()
       context['user_in_group_manager'] = user_in_group_manager
       return context
      
class RecoveryMethodCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   #указываем разработанную форму
   form_class = RecoveryMethodsForm
   #модель машин
   model = RecoveryMethod
   # и новый шаблон, в котором используется форма
   template_name = 'info/recovery_method_edit.html'
   permission_required = 'info.add_recoverymethod'

class RecoveryMethodUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   #указываем разработанную форму
   form_class = RecoveryMethodsForm
   #модель машин
   model = RecoveryMethod
   # и новый шаблон, в котором используется форма
   template_name = 'info/recovery_method_edit.html'
   permission_required = 'info.change_recoverymethod'

class RecoveryMethodDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   #указываем разработанную форму
   form_class = RecoveryMethodsForm
   #модель машин
   model = RecoveryMethod
   # и новый шаблон, в котором используется форма
   template_name = 'info/recovery_method_delete.html'
   permission_required = 'info.delete_recoverymethod'
      
class ClientDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = Client
   template_name = 'info/client.html'
   context_object_name = 'client'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         cars = Car.objects.all()
         for car in cars:
            client = car.client
            if(self.get_object() == client and (car.client.user == ruser or car.service_company.user == ruser)):
               return True
         return False
      
class ServiceCompanyDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
   model = Service_Company
   template_name = 'info/service_company.html'
   context_object_name = 'service_company'

   def test_func(self):
      ruser = self.request.user
      if(ruser.is_superuser or ruser.groups.filter(name='manager').exists()):
         return True
      else:
         cars = Car.objects.all()
         for car in cars:
            service_company = car.service_company
            if(self.get_object() == service_company and (car.client.user == ruser or car.service_company.user == ruser)):
               return True
         return False