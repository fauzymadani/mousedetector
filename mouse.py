import time
import serial
from pynput.mouse import Listener


Arduino = serial.Serial('COM10') #change your COM port
Arduino.baudrate = 9600

def on_click(*args):
    #see what argument is passed
    if args[-1]:
        #do something when the mouse is presssed
        if args[-2].name == "left":
            print('the "{}" mouse key has held down'.format(args[-2].name))
            Arduino.write(str.encode("1"))

    elif not args[-1]:
        #do something when the mouse key is released
        print('the "{}" mouse key is released'.format(args[-2].name))
        Arduino.write(str.encode("0"))

#open listener for mouse key presser
with Listener(on_click=on_click) as listener:
    #listen to the mouse key presses
    listener.join        
