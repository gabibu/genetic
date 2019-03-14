

from abc import ABC, abstractmethod
import random

class Shape(ABC):
    def __init__(self, color):
        self.color = color
        super().__init__(self)

class ColorMutator:

    def mutate(self, color, color_dimension_to_mutate):
        if color_dimension_to_mutate == 'r':
            setter = color.setR
            current_color = color.r
        elif color_dimension_to_mutate == 'g':
            setter = color.setG
            current_color = color.g
        elif color_dimension_to_mutate == 'b':
            setter = color.setB
            current_color = color.b
        else:
            raise Exception('invalid color_dimension_to_mutate paramater {0}'.format(color_dimension_to_mutate))

        start = max(current_color - 50, 0)
        end = min(current_color + 50, 255)

        my_range = end - start
        if my_range < 100:
            missing = 100 - my_range
            if start - missing > 0:
                start = start - missing
            elif end + missing < 255:
                end = end + missing

        new_color = random.randint(start, end)
        setter(new_color)

class ShapeMutator(ABC):

    def __init__(self, color_mutator):
        super().__init__()
        self._color_mutator = color_mutator

    @abstractmethod
    def mutate(self, shape):
        pass



class   CircleMutator(ShapeMutator):

    def __init__(self, config, color_mutator):

        ShapeMutator.__init__(self, color_mutator)
        self.config = config

    def mutate(self, shape):

        mutation = random.randint(0, 5)

        if mutation == 0:

            max_change = int(0.1 * self.config._target_image_width)

            start = int(max(shape._x - int(max_change /2),0))
            end = int(min(shape._x + int(max_change /2), self.config._target_image_width -1))

            my_range = end - start

            if my_range  < max_change:
                missing = max_change - my_range
                if start - missing >=0:
                    start = start - missing
                elif end + missing < self.config._target_image_width -1:
                    end = end + missing

            generated_x = random.randint(start, end)
            shape._x = generated_x

        elif mutation ==1:
            max_change = int(0.1 * self.config._target_image_height)

            start = int(max(shape._y - int(max_change/2), 0))
            end = int(min(shape._y + int(max_change/2), self.config._target_image_height-1))

            my_range = end - start

            if my_range < max_change:
                missing = max_change- my_range
                if start - missing >= 0:
                    start = start - missing
                elif end + missing < self.config._target_image_height -1:
                    end = end + missing

            generated_y = random.randint(start, end)
            shape._y = generated_y

        elif mutation==2:
            radius_limit = int(max(self.config._target_image_width, self.config._target_image_height) / 8)

            radius_possible_change = max(int(0.3 * shape._radius), 1)

            add_radius = random.randint(-radius_possible_change, radius_possible_change)

            generated_radius = (shape._radius + add_radius)
            shape._radius = max(min(generated_radius , radius_limit), 2)


        elif mutation >=3 and mutation <=5:

            if mutation == 3:
                color_dimension ='r'
            elif mutation == 4:
                color_dimension = 'g'
            elif mutation == 5:
                color_dimension = 'b'

            self._color_mutator.mutate(shape.color, color_dimension)

        else:
            raise  Exception('unsupported mutation {0}'.format(mutation))













