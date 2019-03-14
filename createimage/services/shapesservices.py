


import random
import numpy as np

from entities.shapes.circle import Circle
from entities.shapes.color import Color
from entities.individual import ImageIndividual
from genetic.geneticservices import GeneticServices
from entities.shapes.shapestypes import ShapeType

class ShapeServices(GeneticServices):

    def __init__(self, config):
        GeneticServices.__init__(self)
        self._config = config
        max_radius = self.maxRadius()
        self.radius_mean = max_radius / config._max_radius_divide

        self.radius_std = max_radius / config._radius_std_divide

    def randomGene(self):
        return self.randomShape()


    def createPopulation(self):
        population = [self._createIndividual() for _ in range(self._config._population_size)]

        return population


    def _createIndividual(self):
        return ImageIndividual([self.randomShape() for _ in range(random.randint(self._config.individual_min_size,
                                                                           self._config.individual_max_size))])

    def randomShape(self):
        return self._createCircle()

    def _randomRadius(self):
        radius = np.random.normal(self.radius_mean, self.radius_std)

        return self._boundRadius(radius)


    def _boundRadius(self, radius):

        if radius < self._config._min_radius:
            return self._config._min_radius
        elif radius > self.maxRadius():
            return self.maxRadius()
        else:
            return radius

    def _createCircle(self):

        x=  random.randint(0, self._config._target_image_width)
        y = random.randint(0, self._config._target_image_height)

        radius = self._randomRadius()

        return Circle(x, y, radius, self._randomColor())

    def _randomColor(self):
        return self._createColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def _createColor(self, r, g, b):
        return Color(r, g, b)

    def maxRadius(self):
        return int(max(self._config._target_image_width, self._config._target_image_height) / 2)

    def join(self, gene1, gene2, alpha):
        if gene1.shapeType() == ShapeType.Circle and gene2.shapeType() == ShapeType.Circle:

            return self._joinCircle(gene1, gene2, alpha)
        else:
            raise Exception('unsipported shape type 1-> {0} or  2-> {2}'.format(gene1.shapeType(), gene2.shapeType()))


    def _joinCircle(self,gene1, gene2, alpha):

        rnd_val = random.random()
        if rnd_val <= 0.4:
            x = gene1._x
        elif rnd_val <= 0.8:
            x = gene2._x
        else:
            x = (alpha * gene1._x) + (1 - alpha) * gene2._x

        rnd_val = random.random()

        if rnd_val <= 0.4:
            y = gene1._y
        elif rnd_val <= 0.8:
            y = gene2._y
        else:
            y = (alpha * gene1._y) + (1 - alpha) * gene2._y

        rnd_val = random.random()

        if rnd_val <= 0.4:
            radius = gene1._radius
        elif rnd_val <= 0.8:
            radius = gene2._radius
        else:
            radius = (alpha * gene1._radius) + ((1 - alpha) * gene2._radius)


        rnd_val = random.random()

        if rnd_val <= 0.4:
            r = gene1.color.r
        elif rnd_val <= 0.8:
            r = gene2.color.r
        else:
            r = int((alpha * gene1.color.r) + ((1 - alpha) * gene2.color.r))



        if rnd_val <= 0.4:
            g = gene1.color.g
        elif rnd_val <= 0.8:
            g = gene2.color.g
        else:
            g = int((alpha * gene1.color.g) + ((1 - alpha) * gene2.color.g))

        if rnd_val <= 0.4:
            b = gene1.color.b
        elif rnd_val <= 0.8:
            b = gene2.color.b
        else:
            b = int((alpha * gene1.color.b) + ((1 - alpha) * gene2.color.b))

        return Circle(x, y, radius, self._createColor(r, g, b))







