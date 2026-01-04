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

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Lekarz"
        verbose_name_plural = "Lekarze"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    class Status(models.TextChoices):
        PLANNED = 'planned', 'Zaplanowana'
        COMPLETED = 'completed', 'Zakończona'
        CANCELLED = 'cancelled', 'Anulowana'

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='appointments'
    )
    date = models.DateTimeField()
    reason = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNED,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Wizyta"
        verbose_name_plural = "Wizyty"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.pet.name} {self.date:%Y-%m-%d %H:%M}"