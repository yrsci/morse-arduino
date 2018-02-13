#!/usr/bin/python3

"""
Created on Mon Sep 11 19:47:32 2017

@author: Yv

Playing with Python & Arduino via PySerial. 

This script records physical presses of a Morse key connected to the Arduino
and translates these to alphanumeric characters.

"""

import serial
from time import sleep


# Construct a dictionary of cw code : alphanumeric char pairs: 
dot_dash_str = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. --..-- .-.-.- ---... -.--.- ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ...---"
chars_str = "a b c d e f g h i j k l m n o p q r s t u v w x y z , . : ) 0 1 2 3 4 5 6 7 8 9 #"

dot_dash_list = dot_dash_str.split(" ")
chars_list = chars_str.split(" ")

cw_ref = dict(zip(dot_dash_list, chars_list))


def CW_translate(string):
    """
    A function that takes an input string of CW (Morse code) and returns
    a translated string of alphanumeric characters.
    """
    
    def translate_by_char(cw_words_list) :
        """
        Inner function takes a list of strings & translates to alphanumeric
        characters letter-by-letter. Returns a list of translated words.
        """
        translated_words = []
        
        for i in cw_words_list:
            cw_chars = (i.split(' '))
            
            alpha_chars = ""
        
            for char in cw_chars:
                try:
                    alpha_chars += cw_ref.get(char)
                except:
                    alpha_chars += '_'
                    
            translated_words.append(str(alpha_chars))

        return translated_words

        
    # Split the input CW string into 'words' and divide the words into chars:
    cw_words = string.split('/')
    if cw_words[-1] == '' :
        cw_words = cw_words[:-1]

    alphanum_words = translate_by_char(cw_words)
    
    return alphanum_words


# Set up the serial port for communication & print its name
try:
    ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
    print(ser.name)    
except:
    print('Failed to open port')
    
sleep(1)

# Initialise an empty list to receive the incoming data:
raw_data = []

print('START BEEPING!')

# Read input from the arduino via the serial port.
try:
    while len(raw_data) < 800:
        data = ser.readline()
        raw_data.append(data)
except:
    print('Failure reading data from port.')
    ser.close()


# Clean the data. First, slice the 0 or 1 from each byte. Then concatonate 
# into one string of 0's and 1's.

beep_str = ""

for beep in enumerate(raw_data):
    index = beep[0]
    clean_beep = str(raw_data[index])[2:-3]
    beep_str += clean_beep

# Split the string into segments of continuous 0's or 1's, & build a list.
# This gives a sequence of key presses / gaps between presses, and how
# long they are.

beep_list = ['0']

for i in beep_str:
    if i == beep_list[-1][-1]:
        beep_list[-1] = beep_list[-1] + i
    else:
        beep_list.append(i)

# Chop off the first element, before the first key press
beep_list = beep_list[1:]

# Convert the beeps / gaps to dots, dashes, spaces (between characters) & 
# slashes (between words) & construct the CW string. The string length
# cutoff vals can be tweaked to suit the key operator.
cw_string = ""
for beep in beep_list:
    if int(beep) == 0 and len(beep) > 50 :
        cw_string += "/"
    elif int(beep) == 0 and len(beep) > 12 :
        cw_string += " "
    elif int(beep) != 0 and len(beep) > 20 :
        cw_string += "END"
    elif int(beep) != 0 and len(beep) > 5 :
        cw_string += '-'
    elif int(beep) !=0 and len(beep) > 1 :
        cw_string += '.'

print('CW string generated: ', cw_string)

translated_words =  CW_translate(cw_string)
translation = ""

for word in translated_words:
    translation += word
    translation += ' '
 
print('translation: ', translation.capitalize())

# Close serial port
ser.close()
