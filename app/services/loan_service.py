__all__ = (
    'LoanService',
)

from app.loan.models import LoanRequest
from app.product.models import Product


class LoanService:
    """Service encapsulates loan logic."""

    @classmethod
    def get_contract_manufacturer_ids_with_join(cls, contract_id: int) -> list[int]:
        """Gets uniq manufacturer ids by contract id in one request with join."""
        return (
            LoanRequest.objects.get_loan_requests_by_contract(contract_id=contract_id)
            .values_list('products__manufacturer_id', flat=True)
            .distinct()
        )

    @classmethod
    def get_contract_manufacturer_ids_with_subquery(cls, contract_id: int) -> list[int]:
        """Gets uniq manufacturer ids by contract id in one request with subquery."""
        loan_request_ids = LoanRequest.objects.get_loan_requests_by_contract(
            contract_id=contract_id,
        ).values_list('id', flat=True)
        return (
            Product.objects.filter(loan_request_id__in=loan_request_ids)
            .values_list('manufacturer_id', flat=True)
            .distinct()
        )
