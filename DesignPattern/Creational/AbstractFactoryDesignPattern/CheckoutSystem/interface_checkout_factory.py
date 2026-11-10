from abc import ABC, abstractmethod
from .interface_invoice import Invoice
from .interface_tax import Tax
from .interface_payment import Payment


class CheckoutFactoryInterface(ABC):

    @abstractmethod
    def get_payment(self) -> Payment:
        pass

    @abstractmethod
    def get_tax_calculator(self) -> Tax:
        pass

    @abstractmethod
    def get_invoice(self) -> Invoice:
        pass
