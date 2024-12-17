#CS3610 Final Exam
#December 17, 2024
#Benjamin Roy
#RegButton.py

from typing import Type
from Button import Button
from ControlOverseer import ControlOverseer

class RegButton(Button):
    #
    def __init__(self, name="RegularButton", x: Type[int] = 0, y: Type[int] = 0):
        super().__init__(name)
        #The x and y axis location of the button on the UI. Default location is 0, 0.
        self.__locationx = x
        self.__locationy = y
        #A flag for the button to keep track of whether or not it's currently registered with the control buttons.
        self.__registered = False 
    
    #Setter and getter for x property
    @property
    def locationx(self):
        return self.__locationx
    @locationx.setter
    def locationx(self, newx: Type[int]):
        self.__locationx = newx

    #Setter and getter for y property
    @property
    def locationy(self):
        return self.__locationy
    @locationy.setter
    def locationy(self, newy: Type[int]):
        self.__locationy = newy


    #When a regular button is clicked, toggle its opt-in status and, using a provided reference to the control button overseer, add the button to the subscribers list.
    def click(self, control: Type[ControlOverseer]):
        if self.__registered:
            print(f"Unregistering {self.name} with Control Buttons...")
            control.unregister(self)
            self.__registered = False
        else:
            print(f"Registering {self.name} with Control Buttons...")
            control.register(self)
            self.__registered = True
        print()

    #Moves the button in the specified direction.
    def move(self, dir):
        print(f"{self.name} will attempt to move {dir}...")
        if dir == "Up":
            self.__locationy += 1
            print(f"{self.name} moved up to {self.__locationx}, {self.__locationy}")
        elif dir == "Down":
            self.__locationy -= 1
            print(f"{self.name} moved down to {self.__locationx}, {self.__locationy}")
        elif dir == "Left":
            self.__locationx -= 1
            print(f"{self.name} moved left to {self.__locationx}, {self.__locationy}")
        elif dir == "Right":
            self.__locationx += 1
            print(f"{self.name} moved right to {self.__locationx}, {self.__locationy}")
        else: #If an invalid input is given
            print(f"{self.name} could not recognize the specified direction, and did not move.")
