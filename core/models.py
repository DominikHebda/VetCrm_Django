from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField("Imię", max_length=100)
    last_name = models.CharField("Nazwisko", max_length=100)

    phone = models.CharField(
        "Telefon",
        max_length=20,
        help_text="Numer kontaktowy"
    )
    email = models.EmailField(
        "Email",
        blank=True
    )

    address = models.TextField(
        "Adres",
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    name = models.CharField("Imię", max_length=100)

    species = models.CharField(
        "Gatunek",
        max_length=100,
        help_text="np. pies, kot"
    )
    breed = models.CharField(
        "Rasa",
        max_length=100,
        blank=True
    )
    birth_date = models.DateField(
        "Data urodzenia",
        blank=True,
        null=True
    )

    owner = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="pets",
        verbose_name="Właściciel",
        null=True
    )

    created_at = models.DateTimeField(
        "Data utworzenia",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Zwierzę"
        verbose_name_plural = "Zwierzęta"
        ordering = ["name"]

    def __str__(self):
        breed = f", {self.breed}" if self.breed else ""
        return f"{self.name} ({self.species}{breed})"


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