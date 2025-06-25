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

# June 18

So for this day i redesigned the pcb routing, tracing, shape and the esp32 orientation, so it is now underneath the oled display, it sure looks a lot more polished!

![Captura de pantalla 2025-06-18 110200](https://github.com/user-attachments/assets/dee06836-e253-4202-b311-a16034bc6bd7)

![Captura de pantalla 2025-06-18 110930](https://github.com/user-attachments/assets/c8403e28-4ff7-43d8-983a-384d5a864871)

![Captura de pantalla 2025-06-18 112512](https://github.com/user-attachments/assets/b036f8ba-c28f-4d07-9b09-b22ee8c25af1)

And then i imported the model to fusion and started to make the initial design of the case, i'm leaning on making it retro futuristic, but keeping it basic.

![image](https://github.com/user-attachments/assets/02ff84f5-4833-43f7-a9df-a815a66ab9f1)

Time Spent: 4 hours

# June 20 

Spent some time looking at like retro tech designs, although i didn't wanna get too inmmersed, so i just got a little inspired by what the old playstations looked like and their controllers

![Captura de pantalla 2025-06-20 140720](https://github.com/user-attachments/assets/5d203eed-5ced-4a97-8d24-0cb94ef85740)

It took it's time but i like it a lot, its my second time using fusion so im quite proud lol.

What's next is I wanna do a custom knurled knob for the rotary encoder, and do a cover for the display, and a snap fit typa thing

Time Spent: 3 hours

# June 22

I did a knurled knob for the encoder to make it have a texture, also because it looks clean bro what the helly

![image](https://github.com/user-attachments/assets/e2e4ed34-c7e9-4a78-88bd-8e73f1459721)

I initially worked on making it threaded but after trying and watching a few tutorials a i just didn't quite have it, so i went to just having it be tight fit, or something like that  

![image](https://github.com/user-attachments/assets/e196c0ab-e375-4656-9894-9c527a1c2020)

Also added some sort of supports for the pcb to be in place, and the pink thingy is the battery, and it didn't fit, so i had to scale the bottom case so the battery fits

![image](https://github.com/user-attachments/assets/50633bc5-dcc2-486f-9815-3e2125144e55)

I want to try making the cases snap fit, but i'll ask in the slack for help lol

Time Spent: 3 hours

# June 23
Since i am a beginner in the  electronics worlds, i used ai for feedback and suggestions.

One of those were that i should power the leds from 5v, but i used a 3.7 Li-Po battery, it recommended a dc boost converter (MT3608).

Also since the esp-32 outputs 3.3v logic, and the LEDs require 5v logic, i used a logic level shifter to step up the signal from 3.3 to 5v.

So i'll have to make the cases for those + the ring case that diffuses the led + the snap fit feature for the pcbs case.

I added a switch to power ON/OFF the device, [i forgot i had to do that if i want to solder the battery], and the switch that does not go on the pcb.

![image](https://github.com/user-attachments/assets/af4cc1d7-46f0-45f2-b184-e89ce80322f4)

Time Spent: 2 hours

# June 24 
It was SO DIFFICULT BRO WHAT THE HELLY

OKay, so after spending like 1.5 hours watching tutorials and trying the snap fit thingy (that tbh, looks gross)
![image](https://github.com/user-attachments/assets/e29583a8-f4f8-49df-8d85-7a7676cb8b96)

I came across a [video from Makers Muse] (https://www.youtube.com/watch?v=7JhjhgjchfM&t=150s) showing how to make 3d printable hinges with different techniques.

And i reallyyy liked the simplicity of [this one](https://youtu.be/7JhjhgjchfM?si=51YC1HOzv-ZzKoi6&t=152)
> Picture from the video/technique

![image](https://github.com/user-attachments/assets/17ebe632-f262-4407-a27c-f70f2c147879)

And i wanted to adapt that, to be snap fit-able or that type of thing, after some discoveries of useful functions from fusion (midplane, sphere, offsetting the sketch plane) i came up with this

![image](https://github.com/user-attachments/assets/f717cfdc-f71a-436b-963f-1f532761160b)
![image](https://github.com/user-attachments/assets/100bc9dd-ac07-4603-a8d1-9947e8a38b8a)

It looks super great and it was time for making this but for the cases of the level shifter module and MT3608. I had to make holes for the wire to go through.

Level Shifter Module:
> Holes for the wire

![image](https://github.com/user-attachments/assets/874d3ce3-94b6-45cc-9f3e-f62e730ad101)
> IT FITS!

![image](https://github.com/user-attachments/assets/34a98695-fbd6-4963-b3a3-7ff36bf22433)
> It has it's little supports so it doesn't move as much

![image](https://github.com/user-attachments/assets/c6c9f358-9df5-4099-beb4-e2b7ed6af939)
> And the snap fit feature! Maybe it's tiny, but i could hot glue this so it's okay if that breaks

![image](https://github.com/user-attachments/assets/fea54267-c894-4f80-bd3d-bb3275d945a2)

MT3608:
> Holes for the wire, yeah

![image](https://github.com/user-attachments/assets/1354807a-508e-4aee-8ef1-bcb78e68584e)
> the same, it fits and has the snap fit and all

![image](https://github.com/user-attachments/assets/785a8371-50c7-4d3c-a76f-f35f49494abc)
> and for the pcb it has it's own snap fit

![image](https://github.com/user-attachments/assets/34e9a2b0-be63-486e-a046-696b79b5a474)

And that's 4.5 hours of work, super goated, also im finished with modelling FINALLY. Although i want to add some text on the cases 

So what's next is making the programm: RadiantOS
> Sounds cool

Time Spent: 4.5 hours
