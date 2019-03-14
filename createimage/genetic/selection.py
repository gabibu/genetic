


import random
from operator import attrgetter
import numpy as np
import numpy.random as npr
from abc import ABC, abstractmethod


class Selection(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def select(self, individuals, fit_attr):
        pass


class RouletteSelection(Selection):

    def __init__(self):
        Selection.__init__(self)

    def select(self, individuals, fit_attr):
        get_fitness_call = attrgetter(fit_attr)
        fitness_values = sorted(individuals, key=get_fitness_call)

        tot_sum = sum([get_fitness_call(ind) for ind in individuals])
        # tot_sum = sum(sorted_weights)
        prob = [get_fitness_call(x) / tot_sum for x in fitness_values]
        cum_prob = np.cumsum(prob)
        random_num = random.random()

        for ind, cum_prob_value in zip(fitness_values, cum_prob):
            if random_num < cum_prob_value:
                return ind


class RankSelection(Selection):

    def __init__(self):
        Selection.__init__(self)

    def select(self, individuals, fit_attr):
        get_fitness_call = attrgetter(fit_attr)
        fitness_values = sorted(individuals, key=get_fitness_call)

        sum_values = sum(range(1, len(fitness_values) + 1))
        prob = [(index + 1.0) / sum_values for index, x in enumerate(fitness_values)]

        choice_index = np.random.choice(len(prob), 1, p=prob)

        return fitness_values[choice_index[0]]




class SelectOne(Selection):
    def __init__(self):
        Selection.__init__(self)

    def select(self, individuals, fit_attr):
        get_fitness_call = attrgetter(fit_attr)

        max = sum([get_fitness_call(c) for c in individuals])

        selection_probs = [get_fitness_call(c) / max for c in individuals]

        return individuals[npr.choice(len(individuals), p=selection_probs)]










