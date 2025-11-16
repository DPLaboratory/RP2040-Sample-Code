# License : GPLv2.0
# copyright (c) 2023  Dave Bailey
# Author: Dave Bailey (dbisu, @daveisu)
# Pico and Pico W board support

import time
import board
import displayio
import terminalio
import busio
import digitalio
from digitalio import DigitalInOut, Direction

import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from duckyinpython import *

currentMode = 0;


async def main_loop():
    global button1
    
    button_task = asyncio.create_task(monitor_buttons())
    await asyncio.gather(button_task)
           
asyncio.run(main_loop())