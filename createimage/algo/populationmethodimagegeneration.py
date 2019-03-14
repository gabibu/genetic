import time
import logging

from algo.algometa import GenerateImageAlg

class GeneticImageGeneration(GenerateImageAlg):

    def __init__(self, config, shape_services, fitness_function, cross_over, mutator, selection_method):
        GenerateImageAlg.__init__(self, config)

        self._shape_services = shape_services
        self._fitness_function = fitness_function
        self.mutator = mutator
        self.cross_over = cross_over
        self.selection_method = selection_method


    def generate(self):

        population = self._shape_services.createPopulation()
        best_image = None

        start = time.time()
        prev_min = 0
        while True:
            current = time.time()
            minutes = (current - start)/60

            if int(minutes) > prev_min:
                print(minutes)
                prev_min = minutes

            self._evaluateve(population)

            current_best_individual =  max(population, key= lambda  indv: indv.fitness)
            new_generation = []
            new_generation.append(current_best_individual)


            if best_image is None or best_image.fitness < current_best_individual.fitness:
                logging.info('new best')
                best_image = current_best_individual
                generated_image = best_image.draw(self._config._target_image.width,
                                                  self._config._target_image.height)


                if self._config.intermediate_best_path:
                    generated_image.save(self._config.intermediate_best_path)
                    logging.info('new best in {0}'.format(self._config.intermediate_best_path))

            while len(new_generation) < self._config._population_size:

                indv1 = self.selection_method.select(population, 'fitness')
                indv2 = self.selection_method.select(population, 'fitness')

                childrens = self.cross_over.crossOver(indv1, indv2)

                for child in childrens:
                    self.mutator.mutate(child)
                    new_generation.append(child)

            population = new_generation

