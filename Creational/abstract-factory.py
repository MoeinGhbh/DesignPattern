"""
    Factory design pattern with abstract 
    
    1- creator
    2- product 
    3- client
"""

from abc import ABC,abstractmethod

#-------------------------------------------
class Creator(ABC):
    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        procuct = self.make()
        result = procuct.edit()
        return result

class JsonCreator(Creator):
    def make(self):
        return json()

class XmlCreator(Creator):
    def make(self):
        return xml()
#-------------------------------------------
class Procuct(ABC):
    @abstractmethod
    def edit(self):
        pass

class json(Procuct):
    def edit(self):
        return 'the file is json'

class xml(Procuct):
    def edit(self):
        return 'the file is xml'
#-------------------------------------------
def client(format):
    return format.call_edit()


print(client(XmlCreator()))