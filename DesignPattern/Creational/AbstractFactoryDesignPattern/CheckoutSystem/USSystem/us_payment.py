from ..interface_payment import Payment

class USPayment(Payment):

    def pay(self, amount:float) ->str:
        return f"Stripe charged USD: {amount}"