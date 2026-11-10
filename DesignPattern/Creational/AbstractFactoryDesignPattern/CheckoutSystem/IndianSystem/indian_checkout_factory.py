from ..interface_checkout_factory import CheckoutFactoryInterface
from .indian_invoice import IndianInvoice
from .indian_payment import IndianPayment
from .indian_tax import IndianTax

class IndianCheckoutFactory(CheckoutFactoryInterface):

    def get_payment(self) -> IndianPayment:
        return IndianPayment()

    def get_tax_calculator(self) -> IndianTax:
        return IndianTax()

    def get_invoice(self) -> IndianInvoice:
        return IndianInvoice()
