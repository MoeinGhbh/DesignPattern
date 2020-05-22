"""
    Creational:
        Singleton
"""

class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance==None:
            self._instance= super().__call__()
        return self._instance



class Db(metaclass=Singleton):
    pass

d1 = Db()
d2 = Db()
d3 = Db()

print(id(d1))
print(id(d2))
print(id(d3))
