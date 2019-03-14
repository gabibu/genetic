
from abc import ABC, abstractmethod

from entities.shapes.shapestypes import ShapeType

class Shape(ABC):
    def __init__(self, color):
        self.color = color
        super().__init__()

    @abstractmethod
    def draw(self, image):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def shapeType(self):
        pass


class Circle(Shape):

    def __init__(self, x, y, radius, color):
        Shape.__init__(self, color)

        self._x = x
        self._y = y
        self._radius = radius

    def draw(self, image):
        color = self.color.pack()
        image.ellipse((self._x - self._radius, self._y - self._radius, self._x + self._radius,
                        self._y + self._radius), fill=color, outline = color)

    def copy(self):
        return Circle(self._x, self._y, self._radius, self.color.copy())

    def shapeType(self):
        return ShapeType.Circle
    

