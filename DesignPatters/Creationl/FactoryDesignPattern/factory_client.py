from PaymentSystem.payment_factory import PaymentFactory

selected_method = "upi" 

payment = PaymentFactory.create_payment(selected_method)
print(payment.pay(799))