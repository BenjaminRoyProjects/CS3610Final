#CS3610 Final Exam
#December 17, 2024
#Benjamin Roy
#Button.py

from abc import abstractmethod, ABC
from typing import Type

class Button(ABC):
    def __init__(self, name: Type[str] = "Button"):
        self.__name = name
    
    #Setter and getter for name property
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newname: Type[str]):
        self.__name = newname

    @abstractmethod
    #A method to perform some behavior when clicked.
    def click(self, control):
        pass

    @abstractmethod
    #A method to perform some behavior when sent a move message
    def move(self, dir):
        pass
