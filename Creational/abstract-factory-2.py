"""
	Abstract Factory:
		Car => 1.benz, 2.bmw  => 1.suv, 2.coupe
			benz suv => gla, glc
			bmw suv => x1, x2
			benz coupe => cls, E-class
			bmw coupe => m2, m4
"""

from abc import abstractclassmethod, ABC


class Car(ABC):
    @abstractclassmethod
    def call_suv(self):
        pass

    @abstractclassmethod
    def call_coupe(self):
        pass
# ----------------------------


class Benz(Car):
    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model


class Bmw(Car):
    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model
# --------------------------------------------


class Suv(ABC):
    @abstractclassmethod
    def create_suv(self):
        pass


class Coupe(ABC):
    @abstractclassmethod
    def create_coupe(self):
        pass
# -------------------------


class Gla(Suv, Benz):
    def create_suv(self):
        print('this is Gla suv of Benz')


class Gls(Suv, Benz):
    def create_suv(self):
        print('this is Gls suv of Benz')


class Eclass(Coupe, Benz):
    def create_coupe(self):
        print('this is Eclass coupe benz ')


class Cls(Coupe, Benz):
    def create_coupe(self):
        print('this is cls coupe benz')
# ------------------------------------------------


class X1(Suv, Bmw):
    def create_suv(self):
        print('this is suv bmw ...')


class X7(Suv, Bmw):
    def create_suv(self):
        print('this is suv bmw .... ')


class M1(Coupe, Bmw):
    def create_coupe(self):
        print('this is m1 coupe bmw....')


class M2(Coupe, Bmw):
    def create_coupe(self):
        print('this is m2 coupe bmw....')
# ----------------------------------------------------


def orderSuv(corp, model):
    if issubclass(model, corp):
        suv = corp().call_suv(model())
        suv.create_suv()
    else:
        NameError


def order_coupe(corp, model):
    if issubclass(model, corp):
        coupe = corp().call_coupe(model())
        coupe.create_coupe()
    else:
        NameError


# ------------------------------------------------------------
try:
    orderSuv(Benz, Gls)
except (NameError, ValueError):  # calling Corporation incorrectly will raise NameError, calling Model incorrectly will raise AttributeError
    print('sorry, this brand does not have desigerd model')

try:
	OrderSuv(Bmw, Glc)
except (NameError, AttributeError):
	print('Sorry, we dont have this model....')
