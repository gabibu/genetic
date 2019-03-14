
from abc import ABC, abstractmethod



class GeneticServices(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def randomGene(self):
        pass

    @abstractmethod
    def join(self, individual1, individual2, index, alpha):
        pass



