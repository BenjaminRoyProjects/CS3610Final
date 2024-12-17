#CS3610 Final Exam
#December 17, 2024
#Benjamin Roy
#ControlButton.py

from typing import Type
from Button import Button
from ControlOverseer import ControlOverseer

class ControlButton(Button):
    def __init__(self, name="ControlButton", direction: Type[str]="Up"):
        super().__init__(name)
        self.__direction = direction #The direction assigned to the control button. Registered regular buttons will move this way when this button is clicked.
    
    #Setter and getter for direction property
    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, newdir: Type[str]):
        self.__direction = newdir

    #When a control button is clicked, have the overseer send a message to all subscribed regular buttons to move.
    def click(self, control: Type[ControlOverseer]):
        print(f"Control button {self.name} will move all registered buttons {self.__direction}...")
        control.update(self.__direction) #Passes the overseer the button's assigned movement direction.

    #Don't need to implement actual behavior for this. Only included in case a control button is registered with the overseer.
    def move(self, dir):
        print(f"{self.name} is a Control Button and will not move {dir}.")
        print()
