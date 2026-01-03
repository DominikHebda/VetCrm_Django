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


class Appointment(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    date = models.DateTimeField()
    reason = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Wizyta"
        verbose_name_plural = "Wizyty"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.pet.name} {self.date:%Y-%m-%d %H:%M}"