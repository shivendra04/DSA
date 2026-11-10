from .interface_payment import PaymentMethod

class CreditCardPayment(PaymentMethod):

    def pay(self, amout:float) -> str:
        return f"paid {amout} by credit card"