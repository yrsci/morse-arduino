#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:47:32 2017

@author: Yv
"""

"""

More experimentation with Python & Arduino via PySerial. 

Records physical presses of a Morse key connected to the Arduino.

Aim is to then parse these, classify as 'dot' or 'dash' and 
auto-translate to alphanumeric characters using Morse code.

Ambitious aim is to tweet - in Morse & English? - from the script too.

"""

import serial
from time import sleep

################

## Construct a dictionary of cw code : alphanumeric char pairs:
dot_dash_str = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. --..-- .-.-.- ---... -.--.- ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----."
chars_str = "a b c d e f g h i j k l m n o p q r s t u v w x y z , . : ) 0 1 2 3 4 5 6 7 8 9"

dot_dash_list = dot_dash_str.split(" ")
chars_list = chars_str.split(" ")

cw_ref = dict(zip(dot_dash_list, chars_list))

################

# Set up the serial port for communication & print its name:
ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
print(ser.name)    

sleep(1)

# Initialise an empty list to hold the 'beeps':
beep_list = []

# Read input from the arduino via the serial port; pressing the key returns a 
# string of 1's until the key is released. These key presses are appended to
# the beep_list for parsing.
while len(beep_list) < 10 :
    data = ser.readline()
    # print as we go, sanity check:
    print(data)
    if b'1\n' in data:
        beep_list.append(data)

# print the 'raw data beeps', i.e. the 1's without the 0's
print("Raw beep data from key: ", beep_list)

cleaned_data = []

#for beep in beep_list:
 #   if  len(beep) > 4