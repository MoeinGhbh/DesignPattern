from abc import ABC,abstractclassmethod

#-------------------------------------------
class Director:
    __builder=None

    def setBuilder(self,builder):
        self.__builder=builder

    def getBuilder(self):
        car = Car()
        
        body = self.__builder.getBody()
        car.setBody(body)

        engin=self.__builder.getEngin()
        car.setEngin(engin)

        wheel=self.__builder.getWheel()
        car.setWheel(wheel)

        return car

#-------------------------------------------
class Car:
    def __init__(self):
        self.__engin=None
        self.__wheel=None
        self.__body=None

    def setEngin(self,engin):
        self.__engin=engin
    
    def setWheel(self,wheel):
        self.__wheel= wheel

    def setBody(self,body):
        self.__body=body

    def details(self):
        print(f'Body is {self.__body.shape}')
        print(f'Enginr is {self.__engin.hp}')
        print(f'Wheel is {self.__wheel.size}')
#---------------------------
class Builder(ABC):
    @abstractclassmethod
    def getEngin(self):
        pass
    def getWheel(self):
        pass
    def getBody(self):
        pass

class Benz(Builder):
    def getBody(self):
        body = Body()
        body.shape='suv'
        return body
    
    def getEngin(self):
        engin = Engin()
        engin.hp = 200
        return engin

    def getWheel(self):
        wheel = Wheel()
        wheel.size=22
        return wheel

class Bmw(Builder):
    def getBody(self):
        body = Body()
        body.shape='sedan'
        return body
    
    def getEngin(self):
        engin = Engin()
        engin.hp = 220
        return engin

    def getWheel(self):
        wheel = Wheel()
        wheel.size=18
        return wheel
#---------------------------
class Wheel:
    size=None

class Body:
    shape=None

class Engin:
    hp:None

car1 = Benz()
director = Director()
director.setBuilder(car1)
res = director.getBuilder()
res.details()