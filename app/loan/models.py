__all__ = (
    'Contract',
    'LoanRequest',
)

from django.db import models

from app.core.django.models import AbstractDates
from app.loan.manager import LoanRequestManager


class Contract(AbstractDates):
    """Contract model."""
    class Meta:
        verbose_name = 'contract'
        verbose_name_plural = 'contracts'
        db_table = 'contract'

    def __repr__(self) -> str:
        return f'Contract({self.id})'


class LoanRequest(AbstractDates):
    """Loan request for number of products."""
    contract = models.ForeignKey('Contract', on_delete=models.SET_NULL, null=True, related_name='loan_requests')

    objects = LoanRequestManager()

    class Meta:
        verbose_name = 'loan request'
        verbose_name_plural = 'loan requests'
        db_table = 'loan_request'

    def __repr__(self) -> str:
        return f'LoanRequest({self.id})'
