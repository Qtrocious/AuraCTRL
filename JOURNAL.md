---
title: "AuraCTRL"
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
