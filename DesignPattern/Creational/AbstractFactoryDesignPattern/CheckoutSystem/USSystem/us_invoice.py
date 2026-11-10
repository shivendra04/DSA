from ..interface_invoice import Invoice

class USInvoice(Invoice):

    def create_invoice(self, sub_total:float, tax:float)->str:
        total = sub_total + tax
        return f"US Invoide Subtotal:{sub_total}, tax:{tax}, total:{total}"