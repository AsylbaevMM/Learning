from PoligonalModel import PoligonalModel
from Flash import Flash
from Camera import Camera


class Scene:
    def __init__(self, Models, Flashes, Cameras) -> None:
        self.Id = None
        self.models = Models
        self.Flashes = Flashes
        self.Cameras = Cameras

    def method1(self, arg):
        pass

    def method2(self, arg1, arg2):
        pass