# from abc import ABCMeta, abstractmethod
# class Area (metaclass=ABCMeta):
#     pass
from abc import ABC, abstractmethod




class Area(ABC) :
    @abstractmethod
    def printarea(self):
        return 0
class Rectange (Area):
    def __init__(self):
        self.length = 4
        self.breadth = 6
    # def printarea(self):
    #     return self.length * self.breadth
rec = Rectange()
# print(rec.printarea())