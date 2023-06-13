

class CustomCounter:
    def __init__(self, value = 0):
        self.__value = value
        self.close = False

    @property
    def value(self):
        if self.close:
            raise AttributeError
        return self.__value
    
    def add(self):
        if self.close:
            raise AttributeError
        self.__value += 1

    def __enter__(self):
        return self
    
    def __str__(self):
        return f"CustomCounter({self.__value})"

    def __exit__(self, exc_type, exc_value, traceback):
        self.close = True
        del self.__value
        del self
        return False


obj = CustomCounter()

print(obj)

with obj as example:
    print(obj.value)
    obj.add()
    obj.add()
    print(obj.value)

print(obj)