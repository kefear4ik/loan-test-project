__all__ = (
    'Product',
    'Manufacturer',
)

from django.db import models

from app.core.django.models import AbstractDates


class Product(AbstractDates):
    """Product loan is taken for."""
    name = models.CharField(max_length=255, null=False)

    loan_request = models.ForeignKey('loan.LoanRequest', on_delete=models.CASCADE, related_name='products')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'product'

    def __repr__(self) -> str:
        return f'Product({self.name})'


class Manufacturer(AbstractDates):
    """Product manufacturer."""
    name = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'
        db_table = 'manufacturer'

    def __repr__(self) -> str:
        return f'Manufacturer({self.name})'
