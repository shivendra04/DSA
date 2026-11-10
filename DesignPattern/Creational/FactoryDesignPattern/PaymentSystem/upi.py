from .interface_payment import PaymentMethod

class UPIPayment(PaymentMethod):

    def pay(self, amount:float) -> str:
        return f"paid {amount} by upi method"