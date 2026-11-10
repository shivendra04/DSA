from .interface_payment import PaymentMethod
from .credit_card import CreditCardPayment
from .upi import UPIPayment
from .wallet import WalletPayment

class PaymentFactory:

    pay_mapping = {
        'credit_card' : CreditCardPayment,
        'upi':UPIPayment,
        'wallet':WalletPayment
    }

    @staticmethod
    def create_payment(pay_type:str) -> PaymentMethod:
        pay_class = PaymentFactory.pay_mapping.get(pay_type.lower(), None)
        if pay_class is None:
            raise ValueError(f"Unsupported payment type: {pay_type}")
        return pay_class()
