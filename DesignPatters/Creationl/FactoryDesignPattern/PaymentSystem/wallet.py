from .interface_payment import PaymentMethod


class WalletPayment(PaymentMethod):

    def pay(self, amount:float)->str:
        return f"paid {amount} by wallet method"