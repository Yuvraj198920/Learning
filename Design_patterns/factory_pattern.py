from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object():
        "An Abstract interface method"

class ConcreteProductA(IProduct):
    "A concrete class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    "A concrete class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcrateProductB"

    def create_object(self):
        return self

class Creator:
    "The factory class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == "a":
            return ConcreteProductA()
        if some_property == "b":
            return ConcreteProductB()
        return None

Product = Creator().create_object("b")
print(Product.name)

