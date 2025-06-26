import board
import busio
import ssd1306
import machine
import keypad
import time
from neopixel import Neopixel 
from machine import Pin, I2C
from keypad import Keypad
from time import sleep

# oled display setup
i2c = I2C(sda=Pin(6), scl=Pin(7))
display = ssd1306.SSD1306_I2C(128,64, i2c)

# Sourced from the micropython docs:
# Will tinker with this when leds arrive
pin = Pin(2, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 7)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour


row_pins = [Pin(10, Pin.OUT), Pin(9, Pin.OUT), Pin(8, Pin.OUT)]
column_pins = [Pin(3, Pin.IN, Pin.PULL_UP),
               Pin(4, Pin.IN, Pin.PULL_UP),
               Pin(5, Pin.IN, Pin.PULL_UP)]

keys = [
    [       'Back',               'D-PadUp',         'Confirm',],
    [     'D-PadLeft',            'Select',         'D-PadRight',],
    ['Sleep Mode De-Activated', 'D-PadDown',    'Sleep Mode Activated'],
]

keypad = Keypad(row_pins, column_pins, keys)

main_menu = ["LEDs", "Animation", "Display"]

led_submenu = ["Back","Blue", "Yellow", "Red", "Custom 1", "Custom 2", "Custom 3"]

anim_submenu = ["Back", "Breathing", "Processing", "Malfunctioning"]

display_submenu = ["Back", "Brightness", "Turn Off After", ""]

menus = {
    "LEDs": led_submenu,
    "Animation": anim_submenu,
    "Display": display_submenu 
}
current_menu = main_menu
selected = 0
in_submenu = False

def draw_selection():
    display.fill(0)
    for i, item in enumerate(current_menu):
        if i == selected:
            prefix = ">" 
        else: 
            prefix = ""
        display.text(f"{prefix} {item}", 0, i * 10)
    display.show()
    
    
while True:
    draw_selection()
    key = keypad.read_keypad()
    
    
    if key == "Down":
        selected = (selected + 1) % len(current_menu)
    elif key == "Up":
        selected = (selected - 1) % len(current_menu)
    elif key == "Sleep Mode Activated":
        machine.deepsleep(1000000)
        
    elif key == "Confirm":
        selected_item = current_menu[selected]
        # rn LEDs options don't exactly do anything much to the leds, but will add it once the hackpad arrive
        if selected_item == "LEDs":
            current_menu = led_submenu
            selected = 0
            in_submenu = True
            if in_submenu and selected_item == "Back":
                current_menu = main_menu
                selected = 0
                in_submenu = False
            else:
                if selected_item == "Blue":
                    np[0] = (0,0,255)
                    np.write()
                    display.fill(0)
                    display.text("LED: Blue", 0,0)
                    display.show()
                    sleep(2)
                    #then ill add for red, yellow, and animations
                    # And ill dim the leds by reducing the rgb values
        elif selected_item == "Animation":
            current_menu = anim_submenu
            selected = 0
            in_submenu = True
            if selected_item == "Back":
                current_menu = main_menu
            elif selected_item == "Breathing":
                display.fill(0)
                display.text(f"Selected: {selected_item}", 0, 0)
                display.show()
                sleep(2)
                current_menu = anim_submenu
                selected = 0 
                in_submenu = True
            elif selected_item == "Processing":
                display.fill(0)
                display.text(f"Selected: {selected_item}", 0, 0)
                display.show()
                sleep(2)
                current_menu = anim_submenu
                selected = 0 
                in_submenu = True
            else:
                selected_item == "Malfunctioning"
                display.fill(0)
                display.text(f"Selected: {selected_item}", 0, 0)
                display.show()
                sleep(2)
                current_menu = anim_submenu
                selected = 0 
                in_submenu = True
                                
        elif selected_item == "Display":
            current_menu = display_submenu
            selected = 0
            in_submenu = True
            if selected_item == "Back":
                current_menu = main_menu
            else:
                selected_item == "Brightness" 
                # Till i have the neopixels + add the rotary encoder funcionatlity to this
                
        else:            
            if in_submenu == True:
                if selected_item == "Back":
                    current_menu == main_menu 
                    selected = 0
                    in_submenu = False
            else : 
                display.fill(0)
                display.text(f"Selected: {selected_item}", 0, 0)
                display.show()
                sleep(2)
                current_menu = main_menu
                selected = 0 
                in_submenu = False