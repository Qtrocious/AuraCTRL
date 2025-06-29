 **Hey, this is my first custom project for Highway!**
# Cool! What is it?
This is an LED ring (that goes in your temple) controlled by a XIAO ESP32-C3 to change it's colors, inspired by the Androids from Detroit: Become Human

# But why tho
I always wanted to be able to create something entirely up from myself, especially if i can wear it @ FRC events! Highway gave me that possiblity

# 3D CASES
These are the MAIN 3d prints for the project, in JOURNAL.md you can see more!

![3d model control](https://github.com/user-attachments/assets/a4392eab-078d-4986-8282-bf9aa315bacd)

This is the LED ring case, more below theres a side view for more visualization

![LED RING CASE](https://github.com/user-attachments/assets/3f19986f-9dd6-4004-a5ec-02502ce583be)
![Analysis view](https://github.com/user-attachments/assets/981fe772-961f-4cc9-885c-880a43f72f22)

# PCB 
My PCB routing and 3d view, enjoy

![PCB 3D](https://github.com/user-attachments/assets/56b5fa7e-72a7-4207-ade0-0e6582589a1a)
![PCB routing](https://github.com/user-attachments/assets/59b5685a-ef8f-4207-8465-93e7dee524a1)

# Wiring outside the PCB
![Soldering](https://github.com/user-attachments/assets/5cd9111c-84c7-4a3e-b18e-069dc7669891)


# BOM
| Item Name                    | Price USD + Shipping | Quantity | Total USD | Justification                                                                 | Purchase Link |
|-----------------------------|-----------------------|----------|-----------|------------------------------------------------------------------------------|---------------|
| XIAO Esp32-C3               | 7.63                  | 1        | 7.63      | To flash the code and use it without being connected to a laptop            | [Aliexpress](https://es.aliexpress.com/item/1005004723068527.html) |
| .96" OLED Display           | 2.65                  | 1        | 2.65      | To select different colors and animations for the LEDs, also to make the XIAO go to deep sleep and so on | [Aliexpress](https://es.aliexpress.com/item/1005006141235306.html) |
| MT3608 Step Up Converter    | 1.60                  | 2        | 1.60      | To step up the 3.7V from the battery into 5V to power the LEDs with sufficient power | [Aliexpress](https://es.aliexpress.com/item/1005006361814667.html) |
| Logic Level Shifter 3v3 to 5v | 0.55                | 1        | 0.55      | To convert the 3.3V logic from the XIAO to 5V logic to give the LEDs good signal | [Aliexpress](https://es.aliexpress.com/item/1005005976067667.html) |
| SS12D00 DIP Slide Switch    | 1.21                  | 20       | 1.21      | To turn on/off everything                                                   | [Aliexpress](https://es.aliexpress.com/item/1000007042312.html) |
| 6x6x15mm Push Button 20 pack | 1.34                 | 20       | 1.34      | To navigate the UI from the OLED                                            | [Aliexpress](https://es.aliexpress.com/item/4001166999847.html) |
| Spirit Gum Adhesive        | 2.36                  | 1        | 2.36      | To stick the LED ring 3D case to the skin, used to glue costume prosthetic to the face | [Aliexpress](https://es.aliexpress.com/item/1005005809932131.html) |
| 3.7 Lipo Battery            | 5.33                  | 1        | 5.33      | To power up everything                                                      | [Aliexpress](https://es.aliexpress.com/item/1005008218024646.html) |
| TP4056 Lithium Battery Charger | 0.99               | 1        | 0.99      | To charge the LiPo Battery without a dedicated charger                      | [Aliexpress](https://www.aliexpress.com/item/1005004427739715.html) |
| 7 SK6812 MINI-E LEDS       | NA                    | 7        | NA        | Comes with the Hackpad kit                                                    ||
| Rotary Encoder             | NA                    | 1        | NA        | Comes with the Hackpad kit                                                    ||  
| **Total with Shipping Cost** | **$30.80**           |          |           |                                                                              ||     
