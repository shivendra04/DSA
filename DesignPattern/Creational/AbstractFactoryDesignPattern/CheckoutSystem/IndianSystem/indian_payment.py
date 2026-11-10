from ..interface_payment import Payment

class IndianPayment(Payment):

    def pay(self, amount:float) ->str:
        return f"Razorpay charged INR: {amount}"