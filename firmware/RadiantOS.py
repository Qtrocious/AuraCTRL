import board
import busio
import ssd1306
import neopixel
from machine import Pin, I2C
from keypad import Keypad
from time import sleep




i2c = I2C(sda=Pin(6), scl=Pin(7))
display = ssd1306.SSD1306_I2C(128,64, i2c)

leds = Pin(2)
led_numbers = 7


row_pins = [Pin(10), Pin(9), Pin(8)]
column_pins = [Pin(3),Pin(4),Pin(5)]

keys = [
    ['1', '2', '3',],
    ['4', '5', '6',],
    ['7', '8', '9'],
]

keypad = Keypad(row_pins, column_pins, keys)

while True:
    key_pressed = keypad.read_keypad()
    if key_pressed:
        print("Key pressed: ", key_pressed)
        display.text("Welcome to RadiantOS")
    sleep(0.1)