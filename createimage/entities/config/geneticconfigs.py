
from utils.imageutils import readImage

class AlgoParams:

    def __init__(self, **kwargs):


        missing = []
        if 'population_size' in kwargs:
            self._population_size = kwargs['population_size']
        else:
            missing.append('population_size')

        if 'min_individual_size' in kwargs:
            self.individual_min_size = kwargs['min_individual_size']
        else:
            missing.append('individual_min_size')


        if 'max_individual_size' in kwargs:
            self.individual_max_size = kwargs['max_individual_size']
        else:
            missing.append('max_individual_size')

        if 'mutation_probability' in kwargs:
            self.mutation_probability = kwargs['mutation_probability']
        else:
            missing.append('mutation_probability')

        if 'intermediate_best_path' in kwargs:
            self.intermediate_best_path = kwargs['intermediate_best_path']
        else:
            self.intermediate_best_path = None


        if 'terget_image_path' in kwargs:
            self._target_image = readImage(kwargs['terget_image_path'])
        else:
            missing.append('terget_image_path')

        if 'min_radius' in kwargs:
            self._min_radius = kwargs['min_radius']
        else:
            missing.append('min_radius')


        if 'max_radius_divide' in kwargs:
            self._max_radius_divide = kwargs['max_radius_divide']
        else:
            missing.append('max_radius_divide')

        if 'radius_std_divide' in kwargs:
            self._radius_std_divide = kwargs['radius_std_divide']
        else:
            missing.append('radius_std_divide')

        if missing:
            raise Exception('Missing paramaters {0}'.format(','.join(missing)))



    @property
    def _target_image_width(self):
        return self._target_image.width

    @property
    def _target_image_height(self):
        return self._target_image.height



