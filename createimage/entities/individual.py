
from PIL import Image, ImageDraw
import numpy as np

from genetic.geneticentities import Individual

class ImageIndividual(Individual):

    def __init__(self, dna, fitness = None):
        Individual.__init__(self, dna, fitness)

    def draw(self, width, height):
        backgroud_color = self._avgColor()

        im = Image.new('RGB', (width, height), backgroud_color)
        dr = ImageDraw.Draw(im)

        for gene in self.dna:
            gene.draw(dr)

        return im

    def copy(self):
        return ImageIndividual([gene.copy() for gene in self.dna])

    def _avgColor(self):
        r = []
        g = []
        b = []

        for gene in self.dna:
            r.append(gene.color.r)
            g.append(gene.color.g)
            b.append(gene.color.b)

        return (np.mean(r).astype(int).item(), np.mean(g).astype(int).item(), np.mean(b).astype(int).item())


