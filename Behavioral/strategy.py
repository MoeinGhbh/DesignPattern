'''
    Strategy
'''
from abc import ABC, abstractclassmethod


class Context:
    def __init__(self, direction, sentance):
        self.sentance = sentance
        self._directition = direction

    @property
    def direction(self):
        return self._directition

    @direction.setter
    def direction(self, dir):
        self._directition = dir

    def sort(self):
        return self._directition.direct(self.sentance)


class Direction(ABC):
    @abstractclassmethod
    def direct(self, data):
        pass


class Left(Direction):
    def direct(self, data):
        print(data)


class Right(Direction):
    def direct(self, data):
        print(data[::-1])


# cntx = Context(Right(), 'Hello world..........!')
cntx = Context(Left(), 'Hello world..........!')
cntx.sort()

