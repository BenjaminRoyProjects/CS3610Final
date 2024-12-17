#CS3610 Final Exam
#December 17, 2024
#Benjamin Roy
#Client.py

from RegButton import RegButton
from ControlButton import ControlButton
from ControlOverseer import ControlOverseer

#Create control buttons
upConButton = ControlButton(name="UpButton", direction="Up")
downConButton = ControlButton(name="DownButton", direction="Down")
leftConButton = ControlButton(name="LeftButton", direction="Left")
rightConButton = ControlButton(name="RightButton", direction="Right")

#Create control button overseer (publisher)
control1 = ControlOverseer()

#Create regular buttons
regbutton1 = RegButton(name="button1")
regbutton2 = RegButton(name="button2")

#Mimic usage of regular buttons
regbutton1.click(control1)
upConButton.click(control1)
regbutton2.click(control1)
upConButton.click(control1)
rightConButton.click(control1)
control1.printRegistered()
regbutton1.click(control1)

