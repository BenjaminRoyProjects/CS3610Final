#CS3610 Final Exam
#December 17, 2024
#Benjamin Roy
#ControlOverseer.py

from typing import Type
from Button import Button

#Publisher class
class ControlOverseer():
    def __init__(self):
        self.__registered = [] #A list of regular buttons currently registered to the control buttons.

    #Add a button to the registered list. Allows both control and regular buttons to be added, but does nothing with control buttons.
    def register(self, button: Type[Button]):
        self.__registered.append(button)

    #Remove a button from the registered list.
    def unregister(self, button: Type[Button]):
        #try:
        self.__registered.remove(button)

    #Print the current subscribers.
    def printRegistered(self):
        print("Buttons registered: ", end="")
        for button in self.__registered:
            print(f"{button.name} ", end="")
        print("\n")

    #Send a movement direction to all registered buttons.
    def update(self, dir):
        for regbutton in self.__registered:
            regbutton.move(dir)
        print()
