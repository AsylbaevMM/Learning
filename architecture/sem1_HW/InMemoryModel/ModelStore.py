

class ModelStore:
    def __init__(self, PoligonalModel, Scene, Flash, Camera, ChangeObservers):
        self.PoligonalModel = None
        self.Scene = None
        self.Flash = None
        self.Camera = None
        self.ChangeObservers = None

    def GetScena(self, num: int):
        pass

    def NotifyChange(self, ModelChanger):
        pass