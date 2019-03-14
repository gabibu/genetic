
from abc import ABC, abstractmethod
import random

class CrossOver(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def crossOver(self, individual1, individual2):
        pass

class OnePointCrossOver(CrossOver):

    def __init__(self, config, target_class):
        CrossOver.__init__(self)
        self.config = config
        self.target_class = target_class



    def crossOver(self, individual1, individual2):

        min_length = min(len(individual1), len(individual1))

        cut_point = random.randint(0, min_length)

        generated_2_end = [gene.copy() for gene in  individual1.dna[cut_point: ]]
        generated_1_end = [gene.copy() for gene in individual2.dna[cut_point :]]

        generated_1_start = [gene.copy() for gene in individual1.dna[:cut_point]]
        generated_2_start = [gene.copy() for gene in individual2.dna[:cut_point]]

        new_generation_1 = self.target_class(generated_1_start + generated_1_end)
        new_generation_2 = self.target_class(generated_2_start + generated_2_end)

        return [new_generation_1, new_generation_2]

class UniformCrossover(CrossOver):

    def __init__(self, config, target_class):
        CrossOver.__init__(self)
        self.config = config
        self.target_class = target_class

    def crossOver(self, individual1, individual2):
        min_length = min(len(individual1), len(individual2))

        generated_dna1 = []
        generated_dna2 = []

        for index in range(0, min_length):
            if random.random() >= 0.5:
                generated_dna2.append(individual1.dna[index].copy())
                generated_dna1.append(individual2.dna[index].copy())
            else:
                generated_dna1.append(individual1.dna[index].copy())
                generated_dna2.append(individual2.dna[index].copy())

        for index in range(min_length, len(individual1)):
            generated_dna1.append(individual1.dna[index].copy())

        for index in range(min_length, len(individual2)):
            generated_dna2.append(individual2.dna[index].copy())

        new_generation_1 = self.target_class(generated_dna1)
        new_generation_2 = self.target_class(generated_dna2)

        return [new_generation_1, new_generation_2]

class ArithmeticCrossOver(CrossOver):

    def __init__(self, config, target_class, genetic_services):
        CrossOver.__init__(self)
        self.config = config
        self.target_class = target_class
        self.genetic_services = genetic_services

    def crossOver(self, individual1, individual2):

        alpha = random.random()
        min_length = min(len(individual2), len(individual1))

        dna1 = []
        dna2 = []
        for index in range(0, min_length):
            gene1 = individual1.dna[len(individual1) - index - 1]
            gene2 = individual2.dna[len(individual2) - index - 1]

            generated_gene1 = self.genetic_services.join(gene1, gene2, alpha)
            dna1.insert(0, generated_gene1)

            generated_gene2 = self.genetic_services.join(gene2, gene1, alpha)
            dna2.insert(0, generated_gene2)

        for index in range(0, len(individual1) - min_length):
            dna1.insert(0, individual1.dna[len(individual1) - index - min_length - 1].copy())

        for index in range(0, len(individual2) - min_length):
            dna2.insert(0, individual2.dna[len(individual2) - index - min_length - 1].copy())

        generated1 = self.target_class(dna1)
        generated2 = self.target_class(dna2)

        if individual1.fitness >= individual2.fitness:
            if alpha >= 0.5:
                return [generated1]
            else:
                return [generated2]
        else:
            if alpha >= 0.5:
                return [generated2]
            else:
                return [generated1]



        #return [generated1, generated2]













