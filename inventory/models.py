from django.db import models

class Chicken(models.Model):
    HEALTH_STATUS_CHOICES = [
        ('Healthy', 'Healthy'),
        ('Sick', 'Sick'),
        ('Deceased', 'Deceased'),
    ]
    
    name = models.CharField(max_length=50)
    age = models.IntegerField()  # in weeks
    breed = models.CharField(max_length=50)
    health_status = models.CharField(max_length=10, choices=HEALTH_STATUS_CHOICES)
    
    def __str__(self):
        return self.name


class Egg(models.Model):
    chicken = models.ForeignKey(Chicken, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_collected = models.DateField()
    
    def __str__(self):
        return f'{self.chicken.name} - {self.date_collected}'
