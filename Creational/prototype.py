from copy import deepcopy

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Prototype:
    def __init__(self):
        self._object={}

    def register(self,name,obj):
        self._object[name]= obj

    def unregister(self,name):
        del self._object[name]

    def clone(self,name,**kwargs):
        cloneObj= deepcopy(self._object.get(name))
        cloneObj.__dict__.update(kwargs)
        return cloneObj


p1= Person('amir',23)
pro=Prototype()
pro.register('person1',p1)
# personCopy = pro.clone('person1')
personCopy = pro.clone('person1',age=433)
print(personCopy.__dict__)
