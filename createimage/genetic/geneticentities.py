
from abc import ABC, abstractmethod


class Individual(ABC):

    def __init__(self, dna, fitness = None):
        self.dna = dna
        self.fitness = fitness
        ABC.__init__(self)


    def setFitness(self, fitness):
        self.fitness = fitness

    def __len__(self):
        return len(self.dna)

    @abstractmethod
    def copy(self):
        pass

