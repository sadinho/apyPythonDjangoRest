from django.db import models
from creditcard import CreditCardValidator

class CreditCard(models.Model):
    exp_date = models.DateField()
    holder = models.CharField(max_length=255)
    number = models.CharField(max_length=16)  # Não criptografado
    cvv = models.CharField(max_length=4, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        # Antes de salvar, determina a bandeira do cartão
        validator = CreditCardValidator(self.number)
        if validator.is_valid():
            self.brand = validator.get_brand()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand} **** **** **** {self.number[-4:]}"
