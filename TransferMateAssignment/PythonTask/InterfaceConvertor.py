from abc import ABCMeta, abstractmethod

class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'conversion') and
                callable(subclass.conversion))

class InterfaceConvertor(metaclass=ParserMeta):
    pass