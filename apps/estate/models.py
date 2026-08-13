from django.db import models





class Appartment(models.Model):
    TYPE_CHOICES = [
        ("commercial", "Коммерческий"),
        ("residential", "Жилой"),
        ("penthouse", "Пентхаус")
    ]
    
    
    number = models.IntegerField(verbose_name="Номер квартиры")
    area = models.FloatField(verbose_name="Площадь")
    floor = models.IntegerField(verbose_name="Этаж")  
    rooms_count = models.IntegerField(verbose_name="Количество комнат")
    deadline = models.DateField(verbose_name="Срок сдачи")
    type = models.CharField(max_length=20,choices=TYPE_CHOICES , verbose_name="Тип") 
    block = models.ForeignKey('Block', on_delete=models.PROTECT, related_name="apartments", verbose_name="Блок" , null= True)
    
    
    
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        unique_together = ('number', 'block') # i
    def __str__(self):
        return f"Квартира {self.number} - {self.area} м² - {self.floor} этаж - {self.rooms_count} комнат - Срок сдачи: {self.deadline} - Тип: {self.type}"
    
 
class Object(models.Model):
    name = models.CharField(max_length=200 , verbose_name="Название объекта")
    number = models.IntegerField(verbose_name="Номер объекта")  
    description = models.TextField(verbose_name="Описание объекта")
    image = models.ImageField(verbose_name="Изображение объекта" , upload_to="estate/images/")
    addres = models.CharField(max_length= 100 , verbose_name="Адрес")
    
    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
    
    
class Block(models.Model):
    number = models.IntegerField(verbose_name="Номер блока")
    floors_count = models.PositiveIntegerField(verbose_name="Количество этажей")
    entrance_count = models.PositiveIntegerField(verbose_name="Количество подъездов")
    image = models.ImageField(verbose_name="Изображение блока" , upload_to="estate/images/")
    object = models.ForeignKey(Object, on_delete=models.PROTECT, related_name="blocks", verbose_name="Объект")
    
    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"
        unique_together = ('object' , 'number')
        
        
    def __str__(self):
        return f"Блок {self.number} - {self.floors_count} этажей - {self.entrance_count} подъездов"   
    
    
