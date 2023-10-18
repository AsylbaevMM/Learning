from Poligon import Poligon
from Texture import Texture


class PoligonalModel:
    def __init__(self, Poligons: list[Poligon], Textures: list[Texture]):
        self.Poligons = Poligons
        self.Textures = Textures