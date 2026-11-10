from ..interface_tax import Tax

class USTax(Tax):
    SALES_TAX_RATE = 0.08

    def calculate_tax(self, sub_total:float) -> float:
        return sub_total * self.SALES_TAX_RATE