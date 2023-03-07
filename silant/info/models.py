from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#справочники, связанные с сущностью Машина
class TechniqueModel(models.Model):
    title = models.CharField(max_length = 64)   #название
    description = models.TextField()            #описание

class EngineModel(models.Model):
    title = models.CharField(max_length = 64)   #название
    description = models.TextField()            #описание

class TransmissionModel(models.Model):
    title = models.CharField(max_length = 64)   #название
    description = models.TextField()            #описание

class DriveAxleModel(models.Model):
    title = models.CharField(max_length = 64)   #название
    description = models.TextField()            #описание

class SteerableBridgeModel(models.Model):
    title = models.CharField(max_length = 64)   #название
    description = models.TextField()            #описание

class TypeOfMaintenance(models.Model):
    title = models.CharField(max_length = 64)   #название
    description = models.TextField()            #описание

class NatureOfFailure(models.Model):
    title = models.CharField(max_length = 64)   #название
    description = models.TextField()            #описание

class RecoveryMethod(models.Model):
    title = models.CharField(max_length = 64)   #название
    description = models.TextField()            #описание

class Service_Company(models.Model):                                      #отдельный справочник для пользователей с соответствующими правами
    user = models.OneToOneField(User, on_delete = models.CASCADE)         #связь один к одному с User
    title = models.CharField(max_length = 64)                             #название
    description = models.TextField()                                      #описание

class Client(models.Model):                                                                     #отдельный справочник для пользователей с соответствующими правами
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user_cl')     #связь один к одному с User
    title = models.CharField(max_length = 64)                                                   #название
    description = models.TextField()                                                            #описание

class Car(models.Model):                                                                             #машина
    machine_serial_number = models.CharField(max_length = 64)                                        #зав. N. машины
    technique_model = models.ForeignKey(TechniqueModel, on_delete = models.CASCADE)                  #модель техники
    engine_model = models.ForeignKey(EngineModel, on_delete = models.CASCADE)                        #модель двигателя
    engine_serial_number = models.CharField(max_length = 64)                                         #зав. N. двигателя
    transmission_model = models.ForeignKey(TransmissionModel, on_delete = models.CASCADE)            #модель ведущей трансмиссии
    transmission_serial_number = models.CharField(max_length = 64)                                   #зав N. ведущей трансмиссии
    drive_axle_model = models.ForeignKey(DriveAxleModel, on_delete = models.CASCADE)                 #модель ведущего моста
    drive_axle_serial_number = models.CharField(max_length = 64)                                     #зав N. ведущего моста
    steerable_bridge_model = models.ForeignKey(SteerableBridgeModel, on_delete = models.CASCADE)     #модель управляемого моста
    steerable_bridge_serial_number = models.CharField(max_length = 64)                               #зав. N управляемого моста
    supply_contract = models.CharField(max_length = 64)                                              #договор поставки N, дата
    date_of_shipment = models.DateField()                                                            #дата отгрузки с завода
    end_user = models.CharField(max_length = 64)                                                     #конечный потребитель(грузополучатель)
    delivery_address = models.CharField(max_length = 64)                                             #адрес поставки(эксплутации)
    equipment = models.CharField(max_length = 64)                                                    #комплектация(доп. опции)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)                                   #клиент
    service_company = models.ForeignKey(Service_Company, on_delete = models.CASCADE)                 #сервисная компания

    #добавим метод для явного указания страницы, на которую нужно перейти после создания машины
    def get_absolute_url(self):
        return reverse('car_detail', args = [str(self.id)])

class Maintenance(models.Model):                                                         #TO
    type = models.ForeignKey(TypeOfMaintenance, on_delete = models.CASCADE)              #вид ТО
    date = models.DateField()                                                            #дата проведения ТО
    operating = models.PositiveIntegerField(default = 0)                                 #наработка, м/час
    orders_number = models.CharField(max_length = 64)                                    #№ заказ-наряда
    orders_date = models.DateField()                                                     #дата заказ-наряда
    organization = models.CharField(max_length = 64)                                     #Организация, проводившая ТО
    car = models.ForeignKey(Car, on_delete = models.CASCADE)                             #машина (экземпляр сущности Car может быть связан более чем с одним экз. сущ. Maintenance)
    service_company = models.ForeignKey(Service_Company, on_delete = models.CASCADE)     #сервисная компания

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('maintenance_detail', args = [str(self.id)])

class Complaint(models.Model):                                                           #Рекламация
    orders_date = models.DateField()                                                     #дата отказа
    operating = models.PositiveIntegerField(default = 0)                                 #наработка, м/час
    order_note = models.ForeignKey(NatureOfFailure, on_delete = models.CASCADE)          #узел отказа
    order_description = models.TextField()                                               #описание отказа
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete = models.CASCADE)      #способ восстановления
    used_spare_parts = models.TextField()                                                #используемые запасные части
    recovery_date = models.DateField()                                                   #дата восстановления
    downtime = models.IntegerField(default = 0)                                          #время простоя техники
    car = models.ForeignKey(Car, on_delete = models.CASCADE)                             #машина
    service_company = models.ForeignKey(Service_Company, on_delete = models.CASCADE)     #сервисная компания

    class Meta:
        ordering = ['-orders_date']

    def get_absolute_url(self):
        return reverse('complaint_detail', args = [str(self.id)])