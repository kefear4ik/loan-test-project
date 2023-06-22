__all__ = (
    'LoanRequestManager',
)


from django.db import models
from django.db.models import QuerySet


class LoanRequestManager(models.Manager):
    def get_loan_requests_by_contract(self, contract_id: int) -> QuerySet:
        return self.filter(contract_id=contract_id)
