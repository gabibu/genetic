
from algo.populationmethodimagegeneration import GeneticImageGeneration
from genetic.fitness import AbsoluteDiffPercentageFitness
from genetic.crossover import OnePointCrossOver, ArithmeticCrossOver, UniformCrossover
from services.shapesservices import ShapeServices
from genetic.mutation import ProbabilityMutator
from genetic.mutators import CircleMutator, ColorMutator
from entities.shapes.shapestypes import ShapeType
from genetic.selection import RankSelection, SelectOne
from entities.individual import ImageIndividual
from entities.config.geneticconfigs import AlgoParams

class AlgoFactory:

    @staticmethod
    def createAlgo(**kwargs):
        params = AlgoParams(**kwargs)

        shape_service = ShapeServices(params)
        fitness_method = AlgoFactory._createFitnessMethod(params, **kwargs)
        cross_over_method = AlgoFactory._createCrossOver(params,  shape_service, **kwargs)
        mutator = AlgoFactory._createMutator(params, **kwargs)
        selector = AlgoFactory._createSelectionMethod(**kwargs)

        return GeneticImageGeneration(params, shape_service,
                                      fitness_method, cross_over_method, mutator, selector)

    @staticmethod
    def _createFitnessMethod(config, **kwargs):

        if 'fiteness_type' not in kwargs:
            raise Exception('missing fiteness_type')

        fitness_type = kwargs['fiteness_type']

        if fitness_type == 'absolute_difference':
            return AbsoluteDiffPercentageFitness(config)
        else:
            raise Exception('unsupported fitness_type {0}'.format(fitness_type))

    @staticmethod
    def _createCrossOver(config, shape_service, **kwargs):

        if 'cross_over_type' not in kwargs:
            raise Exception('missing cross_over_type')

        cross_over_type = kwargs['cross_over_type']
        if cross_over_type == 'uniform':
            return UniformCrossover(config, ImageIndividual)
        elif cross_over_type == 'one_point':
            return OnePointCrossOver(config, ImageIndividual)
        elif cross_over_type == 'arithmetic':
            return ArithmeticCrossOver(config, ImageIndividual, shape_service)
        else:
            raise Exception('unsupported cross_over_type {0}'.format(cross_over_type))

    @staticmethod
    def _createMutator(config, **kwargs):

        if 'mutator_type' not in kwargs:
            raise Exception('missing mutator_type')

        mutator_type  = kwargs['mutator_type']

        if mutator_type == 'probability':
            return ProbabilityMutator(config, {ShapeType.Circle: CircleMutator(config, ColorMutator())})
        else:
            raise Exception('unsupported mutator_type {0}'.format(mutator_type))


    @staticmethod
    def _createSelectionMethod(**kwargs):

        if 'selection_method' not in kwargs:
            raise Exception('missing selection_method ')

        selection_method = kwargs['selection_method']

        if selection_method == 'rank':
            return RankSelection()

        elif selection_method == 'selectone':
             return SelectOne()
        else:
            raise Exception('unsupported selection_method {0}'.format(selection_method))



