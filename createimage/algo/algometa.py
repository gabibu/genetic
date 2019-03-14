
from abc import ABC, abstractmethod


class GenerateImageAlg(ABC):

    def __init__(self, config):
        super().__init__()

        self._config = config

    @abstractmethod
    def generate(self):
        pass


    def _evaluateve(self, population):

        for individual in population:
            individual_fitness = self._fitness_function.fitness(individual, self._config._target_image)
            individual.fitness = individual_fitness
