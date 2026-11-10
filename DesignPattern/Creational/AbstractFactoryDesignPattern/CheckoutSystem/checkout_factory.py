from .IndianSystem.indian_checkout_factory import IndianCheckoutFactory
from .USSystem.us_checkout_factory import USCheckoutFactory
from .interface_checkout_factory import CheckoutFactoryInterface

class CheckoutFactory:

    factories: dict[str, type[CheckoutFactoryInterface]] = {'india':IndianCheckoutFactory,
                 'us':USCheckoutFactory}
    
    @staticmethod
    def get_checkout_factory(country:str)->CheckoutFactoryInterface:
        try:
            return CheckoutFactory.factories[country.lower()]()
        except KeyError as error:
            available_countries = ", ".join(CheckoutFactory.factories)
            raise ValueError(
                f"Unsupported country '{country}'. "
                f"Supported countries: {available_countries}."
            ) from error
