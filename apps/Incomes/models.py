from django.db import models


class Income(models.Model):
    source = models.CharField(max_length=225)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.source} - {self.amount}"
    