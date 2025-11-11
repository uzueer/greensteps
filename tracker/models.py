from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class EmissionFactor(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200)
    co2_per_unit = models.DecimalField(max_digits=10, decimal_places=4)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.activity_name} ({self.co2_per_unit} kg CO2/{self.unit})"

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    emission_factor = models.ForeignKey(EmissionFactor, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['-date', '-created_at']

    @property
    def total_emissions(self):
        return float(self.quantity) * float(self.emission_factor.co2_per_unit)

    def __str__(self):
        return f"{self.user.username} - {self.emission_factor.activity_name} on {self.date}"
