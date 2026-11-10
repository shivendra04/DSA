from ..interface_tax import Tax

class IndianTax(Tax):
    GST_RATE = 0.18

    def calculate_tax(self, sub_total:float) -> float:
        return sub_total * self.GST_RATE