#!/usr/bin/env python
import time
import os
import os.path
from pyA20.gpio import gpio
from pyA20.gpio import port
import subprocess
from actions import stop

gpio.init()

#Stopbutton
gpio.setcfg(port.PA16, gpio.INPUT)
gpio.pullup(port.PA16, gpio.PULLUP)

while gpio.input(port.PA16):
    time.sleep(0.01)
    if not gpio.input(port.PA16):
       print('Stopped')
       stop() 
