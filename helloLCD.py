#!/usr/bin/python
#show "Hello World on the LCD screen"
#

import Adafruit_CharLCD as LCD
import time

lcd = LCD.Adafruit_CharLCDPlate()

displaytext = "Hello World"

lcd.clear()
lcd.message(displaytext)

while (True):
    if lcd.is_pressed(LCD.UP):
        lcd.set_backlight(1)
        lcd.message(displaytext)

    else:
        lcd.set_backlight(0)
        lcd.clear()
        time.sleep(0.5)