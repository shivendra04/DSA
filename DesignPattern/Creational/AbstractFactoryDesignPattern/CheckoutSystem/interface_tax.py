from abc import ABC, abstractmethod

class Tax(ABC):

    @abstractmethod
    def calculate_tax(self, sub_total:float)->float:
        pass