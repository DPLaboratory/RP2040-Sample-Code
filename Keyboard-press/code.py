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

# Button mapping
#
#  BTN1   BTN2   BTN3
#  BTN4   BTN5   BTN6
#  

# Start Setting
BTN1_PIN = board.GP9
BTN2_PIN = board.GP8
BTN3_PIN = board.GP7
BTN4_PIN = board.GP6
BTN5_PIN = board.GP5
BTN6_PIN = board.GP4

buttons = [
    digitalio.DigitalInOut(BTN1_PIN),
    digitalio.DigitalInOut(BTN2_PIN),
    digitalio.DigitalInOut(BTN3_PIN),
    digitalio.DigitalInOut(BTN4_PIN),
    digitalio.DigitalInOut(BTN5_PIN),
    digitalio.DigitalInOut(BTN6_PIN)
]

for i in range(0,6):
    buttons[i].direction = digitalio.Direction.INPUT
    buttons[i].pull = digitalio.Pull.DOWN
    

currentMode = 0;

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def handle_mode_press(key):
    layout.write('ciao\n')
    

# Mantiene il programma attivo
while True:
    for btn in range(0, 6):
        if buttons[btn].value:  # Il pulsante è premuto (valore basso)
            print("currentMode pre : ", currentMode, "btn:", btn)
            handle_mode_press(btn)
            print("currentMode dop :", currentMode, "btn:", btn)
           
    time.sleep(0.2)