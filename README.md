# TestHomeAutomation
HomeAutomation using a Wemos D1 Mini, Servo Motor (180 degree), LED. iOS App using Kivy - Python.

Hardware Requirements:
1. Wemos D1 Mini ESP8266 - https://www.amazon.in/gp/product/B077MDHLRC/
2. Servo Motor (180 Degrees) - https://www.amazon.in/gp/product/B00MTFFAE0/

Wemos D1 Mini Pinout:
![](https://escapequotes.net/wp-content/uploads/2016/02/esp8266-wemos-d1-mini-pinout.png)

Tools Needed:
1. Arduino IDE 
2. Python >= 3.6
3. XCode

Setup Instructions:

* IDE Setup
  1. Download and Install the Arduino IDE from https://www.arduino.cc/en/main/software
  2. Open Arduino > Preferences > Additional Board Manager URLs: http://arduino.esp8266.com/stable/package_esp8266com_index.json. Click OK.
  3. Open Tools > Board > Boards Manager. Type esp in the search bar, and Install "esp8266 by ESP8266 Community". Click OK.
  4. Open Tools > Board. Select Wemos D1 R1.
  5. Paste the WemosD1.ino code inside the file. Change the ssid, password and gateway according to your router and save it.
  6. Connect the ESP8266 module via USB. Select your USB Port from Tools > Port.
  7. Connect a LED to GPIO Pin D5 and G. 
  7. Upload the Sketch using Sketch > Upload.
  8. Open Browser and go to the static ip for the module: http://192.168.0.123/
  9. Use the Links to switch On/Off the LED.
