
import argparse
import logging
import sys

from algo.algofactory import AlgoFactory
from entities.config.geneticconfigs import AlgoParams
from utils.imageutils import readImage

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
from utils.yaml import readConf










if __name__ == '__main__':
    parser = argparse.ArgumentParser("imagegenerationservice")
    # parser.add_argument('--population_size', metavar='population_size', type=int, required=True)
    # parser.add_argument('--min_individual_size', metavar='min_individual_size', type=int, required=True)
    # parser.add_argument('--max_individual_size', metavar='max_individual_size', type=int, required=True)
    # parser.add_argument('--terget_image_path', metavar='terget_image_path', required=True)
    # parser.add_argument('--mutation_probability', metavar='mutation_probability', type=float, required=True)
    # parser.add_argument('--intermediate_best_path', metavar='intermidiate_best_path', required=False)
    #



    parser.add_argument('--conf_file', metavar='conf_file', required=True)

    paramaters = parser.parse_args()

    config = readConf(paramaters.conf_file)



    # params = AlgoParams(paramaters.population_size, paramaters.min_individual_size, paramaters.max_individual_size,
    #                     target_image, paramaters.mutation_probability, paramaters.intermediate_best_path)






    algo = AlgoFactory.createAlgo(**config)
    algo.generate()



