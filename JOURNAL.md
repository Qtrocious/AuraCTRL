---
title: "Radiant"
author: "@Qtrocious"
description: "An LED ring that goes in your temple, inspired by the Androids from Detroit: Become Human!"
created_at: "2025-06-12"
---

# June 12 

This is my second project and my first custom project!

Today i started to brainstorm. And i wanted to make something simple but super cool.

After sometime of brainstorming ideas, I got with making a simple but super cool project, with my new experience in fusion and kicad, I got to the idea of making the LED ring that the android from DBH have on their temple, they serve the purpose of showing processing operations, damage caused, and other things.

In the robotics events (FRC) I went to, I saw a few teams that controlled the robot have some kind of wearable tech, and it ALWAYS looked cool asf.

So with that in mind i wanted to change the purpose of the led ring, when competing with other robots, scouting data from other teams robots, or just showing that you're chilling. I wanted to show a different color + be configurable with those sk6812 mini-e leds that i didn't used from hackpad!

I didn't want to worry about cables and all of that, so that's the reason i'll be shooting for making it wireless, this is a HUGE jump from me, let's hope it works lol.

After researching and getting the help of some concepts with chatgpt and deepseek (l learned about ble tech, types of esp32, mcu, the differences between micropython and circuitpython), i went with this

- Seeed Studio XIAO ESP32-C3: For the micro controller
> So, bluetooth is out the way, because it'll require two different Xiaos, and that would cost more, so, i'll just stick with making it with wires

- The 7 SK6812 MINI-E LEDS i didn't used from the Hackpad approved parts, that will save more money!

- Also the rotary encoder from Hackpad

Time spent: 2 hours

# June 13 

Started to try to make the shape of the pcb and placing out all the components.

I already had the footprint of the sk6812 led, rotary encoder, what's yet to be determined is the button.

I wanna make 3d printed buttons that go over the buttons so it looks more professional, but first i need to find which. 

> Im leaning over the push buttons with the 6x6x12mm, so i can fit the 3d part and make it stick to the button, also maybe a display to select color and animation of led, plus with a rotary encoder, animation speed

![Captura de pantalla 2025-06-13 163717](https://github.com/user-attachments/assets/bc36951d-31d4-4fde-9fed-77ddd957c63d)

> The outer circle is 40mm in diameter and the inner is 20mm

![Captura de pantalla 2025-06-14 001225](https://github.com/user-attachments/assets/2bf4e900-c1ad-488f-8a8d-f859ad23b71d)

I put in an array of circular thingy tool form kicad to place it right.

![Captura de pantalla 2025-06-14 001236](https://github.com/user-attachments/assets/e258816f-28cf-435e-9e4c-a35ff718d3d8)

Traced the components and added the buttons in a matrix of 3x3, and tomorrow adding the display, maybe a 128x64 just to see how it would turn out!

![image](https://github.com/user-attachments/assets/4b44fae3-b550-45f3-b58e-73520b7d1b32)

> Here you can see the buttons and the rotary encoder. 

So i know there are certain pcb that come with modules, but are separated by a thin line of pcb board, so you can easily break them, they are called breakable pcb module, or mouse bites, well since i'll be essentially making two pcbs, this is perfect for that!

> Don't want to say this took a lot of time but this took a lot of time TT

I'll still need to figure out how to do that, i think i almost got it.

I also wanted to make a 3d model of the control for the call with Scotty from Strange Parts! It helped me a lot to visualize it further

I present you the first iteration of the AuraCTRL case 

![image](https://github.com/user-attachments/assets/e2df5dd9-a92c-4ea1-9319-c90c2a847d2f)
![Captura de pantalla 2025-06-13 164034](https://github.com/user-attachments/assets/c9067f3f-b7dc-442e-8432-e6f187fab371)
![Captura de pantalla 2025-06-13 164057](https://github.com/user-attachments/assets/c5455b65-a8e4-4339-8802-9a49cef005f1)

> It will slide but have enough grip to keep it in place, it will be around the wrist, i still need to learn about maybe how to make it adjustable so everyone can use it, maybe take inspiration from the pip boy project!

Time Spent: 8 hours

# June 14
Been researching what cables are common for pcb, and learned about AWG, so for simple connections i'll need long 22 AWG cables, luckily a friend knows a store called "Electrónica Para Estudiantes" and they sell 3 meters of it for half a dollar!
> what the helly

Added the display, with 3d model from [grabcad](https://grabcad.com/library/display-oled-ssd1306-de-0-96-1) and [footprint](https://github.com/pforrmi/KiCad-SSD1306-128x64/blob/master/library/SSD1306.pretty/128x64OLED.kicad_mod)

So with the display now on the pcb, i need to change the size of it
And after some time, i placed the parts and build the pcb outline, made the first draft of the v notch (i think its called like that?)
Rewired the neopixels, so what's left is tracing the control module!

Here it looks as of now, it looks like a phone lol

![Pcb and 3d view](https://github.com/user-attachments/assets/e14e00ae-6fcf-48dc-ba71-e31562e78784)


Time Spent: 3.5 hours

# June 15 

> Forgot to journal this day lol

I repositioned the neopixels module board, and had to make some vias so when soldering i put the cables in it so i connect them easily

![Captura de pantalla 2025-06-15 213602](https://github.com/user-attachments/assets/9154d728-4c9b-46e3-ba49-bb3e44021c34)


Time Spent: 1 hour

# June 16

I wanted to start making the first draft of the code, i knew i wanted to use micropython, and since the schematic looks the same as the macropad (i just realized this sorry T-T), i figured i'd research on how to make a keypad matrix on micropython.

Plus how to setup a my display of 128x36, and got the idea of making an interface, going through it with the rotary encoder like an omnitrix lol

So the code looks like this now, im getting used to the logic of this so yeah!

```
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
```



Also Summer of Making launched, super perfect to start redoing the pcb design, adding some silkscreen art omg



Time Spent: 1.5 hours

# June 17
I just opted to round the corners of the pcb and finally started to add some silkscreen art!
I downloaded the svg file from the highway website 

![image](https://github.com/user-attachments/assets/f7419138-5223-4168-be95-67288e898545)

I'll maybe add more art, but it's a **maybe**
Right now i'll export the pcb STEP file to fusion to figure out the shape of the case.

I began importing it, and making some sketches, i needed to recreate the pcbs layout as it was no letting me use the Sketch Dimension

![image](https://github.com/user-attachments/assets/1bc40b6a-ef7c-45c4-9f6f-dd54f09eca79)

![image](https://github.com/user-attachments/assets/ed8676e7-f28d-48f4-ae00-557adbc701f1)


And i found out my pcbs outline is not what i was looking for, which was a sort of control that handled the leds colour which would be strapped in my wrist.

I realized that i could easily make it look like a watch, so i used (Excalidraw)[https://excalidraw.com/] to sketch something up, i actually like it, it less dense, and easily accessible 

![image](https://github.com/user-attachments/assets/217698d6-b7cd-4193-9eb4-252d4d3fb110)

I think i'll base the design on how devices are built in Detroit: Become human maybe even add some leds to the watch also! 

And i'll have to look on how to make custom 3d printed buttons that fit on the push buttons 💀


Time Spent: 4 hours
