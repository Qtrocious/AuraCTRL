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

menu = ["LEDs", "Animation Settings", "Display Settings"]
led_menu = ["Back","Blue Light", "Yellow Light", "Red Light", "Custom light 1", "Custom light 2", "Custom light 3"]

anim_setts = ["Back", "Breathing", "Processing", "Malfunctioning"]

display_setts = ["Back", "Brightness", "Turn Off After", ""]


row_pins = [Pin(10), Pin(9), Pin(8)]
column_pins = [Pin(3),Pin(4),Pin(5)]|

keys = [
    ['Back', 'D-PadUp', 'Confirm',],
    ['D-PadLeft', 'Select', 'D-PadRight',],
    ['Sleep Mode De-Activated', 'D-PadDown', 'Sleep Mode Activated'],
]

keypad = Keypad(row_pins, column_pins, keys)

# while True:
  #  key_pressed = keypad.read_keypad()key
   # if key_pressed:
    #    display.text(key_pressed)
   # sleep(0.1)
    
current_menu = menu
selected = 1

def draw_menu():
    for i, item in enumerate(current_menu):
            if i == selected:
                prefix =">"    
            else:
                prefix = " "
            display.text(f"{prefix} {item}", 0, i * 10)
    display.show()

def draw_ledmenu():
    display.fill(0)
    key_pressed = keypad.read_keypad()
    if current_menu == led_menu and selected == 1:
        display.menu
         
    
