from abc import ABC, abstractmethod

class Invoice(ABC):

    @abstractmethod
    def create_invoice(self, sub_total:float, tax:float)->str:
        pass