from ..interface_checkout_factory import CheckoutFactoryInterface
from .us_invoice import USInvoice
from .us_payment import USPayment
from .us_tax import USTax

class USCheckoutFactory(CheckoutFactoryInterface):

    def get_payment(self) -> USPayment:
        return USPayment()

    def get_tax_calculator(self) -> USTax:
        return USTax()

    def get_invoice(self) -> USInvoice:
        return USInvoice()
