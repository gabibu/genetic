

from PIL import Image


def readImage(path):
    target_image = Image.open(path)
    return target_image


