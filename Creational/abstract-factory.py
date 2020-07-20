"""
	Abstract Factory
		Car => Benz, Bmw => Suv, Coupe
			benz suv => gla, glc
			bmw suv => x1, x2
			benz coupe => cls, E-class
			bmw coupe => m2, m4
"""
from abc import ABC,abstractclassmethod

class Car(ABC):
    @abstractclassmethod
    def call_suv(self):
        pass

    @abstractclassmethod
    def call_coupe(self):
        pass
#---------------------------------------------
class Benz(Car):
    def call_suv(self):
        return Gla()
    def call_coupe(self):
        return Cls()
#---------------------------------------------
class Bmw(Car):
    def call_suv(self):
        return X1()
    def call_coupe(self):
        return M2()
#---------------------------------------------
class SUV(ABC):
    @abstractclassmethod
    def create_suv(self):
        pass

class Coupe(ABC):
    @abstractclassmethod
    def create_coupe(self):
        pass
#------------------------------------------------
        # Benz
class Gla(SUV):
    def create_suv(self):
        print("this is your Gla SUV Benz...")

class Cls(Coupe):
    def create_coupe(self):
        print("this is your cls coupe Benz...")
#---------------------------------------------------
    # BMW
class X1(SUV):
    def create_suv(self):
        print("this is your X1 SUV BMW .... ")

class M2(Coupe):
    def create_coupe(self):
        print("this is your me coupe BMW ....")
#------------------------------------------------------

def client_suv_order(order):
    suv = order.call_suv()
    suv.create_suv()

def client_coupe_order(order):
    coupe= order.call_coupe()
    coupe.create_coupe()

#----------------------------------------------------------
client_coupe_order(Benz())
client_coupe_order(Bmw())

client_suv_order(Benz())
client_suv_order(Bmw())
