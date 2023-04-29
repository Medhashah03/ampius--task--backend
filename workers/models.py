from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    address = models.TextField()
    contact_info = models.CharField(max_length=255)
    safety_breaches = models.PositiveIntegerField(default=0)
    #medical history fields,can be made into a seperate model
    blood_group = models.TextField(max_length = 5)
    health_problem = models.TextField()

    def __str__(self):
        return self.name




