from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField(blank=True, null=True)
    owner_phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Zwierzę"
        verbose_name_plural = "Zwierzęta"

    def __str__(self):
        return f"{self.name} ({self.species}) {self.breed} ({self.birth_date})"