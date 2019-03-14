

class Color:
    def __init__(self, r, g, b):
        self._rgb = [r, g, b]

    def pack(self):
        return tuple(self._rgb)

    def copy(self):
        return Color(self._rgb[0], self._rgb[1], self._rgb[2])

    def setR(self, color):
        self._rgb[0] = color

    def setG(self, color):
        self._rgb[1] = color

    def setB(self, color):
        self._rgb[2] = color

    @property
    def r(self):
        return self._rgb[0]

    @property
    def g(self):
        return self._rgb[1]

    @property
    def b(self):
        return self._rgb[2]