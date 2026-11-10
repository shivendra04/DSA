from CheckoutSystem.checkout_factory import CheckoutFactory
from CheckoutSystem.interface_checkout_factory import CheckoutFactoryInterface


def checkout(sub_total:float, factory:CheckoutFactoryInterface)->None:
    tax = factory.get_tax_calculator().calculate_tax(sub_total)
    invoice = factory.get_invoice().create_invoice(sub_total, tax)
    payment_result = factory.get_payment().pay(sub_total+tax)

    print(invoice)
    print(payment_result)


if __name__ == '__main__':
    indian_factory = CheckoutFactory.get_checkout_factory('india')
    checkout(200, indian_factory)

    print()

    us_factory = CheckoutFactory.get_checkout_factory('us')
    checkout(100, us_factory)

