
import random
from abc import ABC, abstractmethod

class Mutator(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def mutate(self, shape, config):
        pass


class ProbabilityMutator(Mutator):

    def __init__(self, config, shape_mutation):
        Mutator.__init__(self)
        self.config = config
        self.shape_mutation = shape_mutation


    def mutate(self, individual):

        for shape in individual.dna:
            prob = random.random()

            if prob <= self.config.mutation_probability:

                current_shape_type = shape.shapeType()

                if current_shape_type not in self.shape_mutation:
                    raise Exception('missing shape {0} from shape_mutation'.format(shape.shapeType()))

                shape_mutator = self.shape_mutation[current_shape_type]

                shape_mutator.mutate(shape)



