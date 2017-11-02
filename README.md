# morse-arduino
Building a Morse code (cw) tweet machine using Arduino &amp; Python 3

Records physical presses of a clothes peg Morse / CW key connected to the Arduino. 
A simple script is loaded to the Arduino to light an LED and buzz a tone when the key is pressed, as well as read the key press status via serial. 

These data are parsed in Python, classified as 'dot', 'dash' or 'space' and translated to alphanumeric characters using a dictionary of Morse code (using info from https://morsecode.scphillips.com/translator.html)... plus the hashtag character.

(Longer-term aim is to tweet from the script; watch this space.)
