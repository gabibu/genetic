
import numpy as np
from abc import ABC, abstractmethod
from PIL import ImageChops

class Fitness(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def fitness(self, individual, target):
        pass


class AbsoluteDiffPercentageFitness(Fitness):

    def __init__(self, config):
        Fitness.__init__(self)
        self._config = config

    def fitness(self, individual, target_image):




        generated_image = individual.draw(target_image.width, target_image.height)
        target_image_pixels = np.asarray(target_image)
        generated_image_pixels = np.asarray(generated_image)

        #diff = np.sum(np.abs(target_image_pixels - generated_image_pixels))

        diff = np.sum(np.asarray(ImageChops.difference(target_image, generated_image)))

        res = 1.0 - (diff / (255.0 * 3.0 * target_image.width * target_image.height))


        #

        # import math, operator
        # from functools import reduce
        #
        # h = ImageChops.difference(target_image, generated_image).histogram()
        #
        #
        # x12 =  \
        #     math.sqrt(reduce(operator.add, map(lambda h, i: h * (i ** 2), h, range(256))) / (float(generated_image.size[0])
        #                                                                                      * generated_image.size[1]))



        #
        return res














