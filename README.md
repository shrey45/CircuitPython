# CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_Ultrasonic](#CircuitPython_Ultrasonic)
* [CircuitPython LCD](#CircuitPython_LCD)
---

## Hello_CircuitPython

### Description & Code
I made the neopixel on the Metro Express board fade from a blue to a bright pink, and then loop back around to blue. I did this by using variables x, y, and z as the RGB values and adding to them every time it loops around, much like a counter, so that thje color changes everytime and works its way up. Once it clocks out on 255, it resets back to 20.

Here's the code:

```python
import time
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = (.3)
x = 25
y = 25
z = 25

while True:

    dot.fill((x, y, z,))
    time.sleep(.1)
    x = x+1
    if x >= 255:
        x = 20
        y = y+5
    if y >= 255:
        y = 20
        z = z+10
    if z >= 255:
        z = 20
    print(x,y,z)
```

### Evidence


https://user-images.githubusercontent.com/63983735/133448966-b5306d66-d752-42c3-9a0a-a3cd8921a596.mp4


### Wiring
There was no wiring necassary for this assignment, the neopixel was built into the board.
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
It was a but difficult at first to learn to code with a new language and software, so it took a bit of tinkering and googling to figure out how to work this thing. It seems a little bit easier know, but I'm just starting so it'll take a bit more time to feel confident like how I am with Arduino.

## CircuitPython_Servo

### Description & Code

Today(or a couple days ago), I was tasked with making a servo move. I did that. I also used capacitive touch to make the servo sweep back ad forth. Using a for loop is also pretty helpful for that. The main part of the code is below, but I also put a link to the full code if you want to take a look at that.

```python
touch_pad = board.A4
touch1_pad = board.A4

while True:
    if touch.value:
        print("Touched A0")
        my_servo.angle = angle
        if angle < 180:
            angle = angle + 5
        if angle >= 180:
            angle = 180
        print(angle)
```
[Click Here for the Full Code](https://github.com/shrey45/CircuitPython/blob/main/Code/Servo.py)

### Evidence

https://user-images.githubusercontent.com/63983735/133453060-47586578-9ce4-4183-98fa-976e8902bab3.mp4

### Wiring

<img src="https://github.com/hheisig51/VigilantWaddle/blob/main/Diagrams/Renders/CircuitPython_Servo.png?raw=true" width="400">

### Reflection




## CircuitPython_Ultrasonic

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## CircuitPython_LCD

### Description & Code

In this assignment, we use capacitive touch, as used in the [Servo assignment](#CircuitPython_Servo), to printnumbers on an LCD screen. When you press one wire, the direction of counting changes from up to down, and vice versa. The other wire, when pressed, will move the number up by 1 every time it is pressed. The thing is though, every time you press, it will only register one touch. So, if you press and hold, it only counts one time.

```python
import board
import time
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

counter = 0
Switchdir = 1 # This switches the direction counter is moving
SwitchA = 0
SwitchB = 0

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

touch = touchio.TouchIn(board.A0)
touch1 = touchio.TouchIn(board.A4)

while True:
    if touch.value and SwitchB == 0:
        print("Touched A0")
        Switchdir = -Switchdir
    SwitchB = touch.value
    
    if Switchdir <= 0 and touch1.value and SwitchA == 0:
        print("Touched A4")
        lcd.set_cursor_pos(0, 0)
        counter += Switchdir
        lcd.print(str(counter))
        lcd.print(" ")
    SwitchA = touch1.value
    
    if Switchdir >= 0 and touch1.value and SwitchA == 0:
        print("Touched A4")
        lcd.clear()
        counter += Switchdir
        lcd.set_cursor_pos(0, 0)
        lcd.print(str(counter))
        lcd.print(" ")
    SwitchA = touch1.value


```

### Evidence

<img src="https://github.com/inovotn04/CircuitPython/raw/main/Images/LCDGif.gif?raw=true" width="400">

Image Credit [Ian Novotne](https://github.com/inovotn04/CircuitPython/raw/main/Images/LCDGif.gif?raw=true)

### Wiring

<img src="https://github.com/jmuss07/Circuit-Python/raw/main/Images/LCD.PNG?raw=true" width="400">

Image Credit [Josie Muss](https://github.com/jmuss07/Circuit-Python)

### Reflection

This was an interesting LCD assignment. The initial part to just get it to count up and down when you tocuhed it was reay easy, just a few basic command lines. When we got to the spicy part it was a bit more difficut to integrate in some booleans. What really didn't help my case was that I read the assignment wrong, and I though we had to use one wire to go up and the other to go down. SO i spent a lot of time trying to make the wrong code, which I thought was right, and when I did do the right code, I thought it was wrong. That was a mouthful. MORAL OF THE STORY. READ THE ASSIGNMENT PROPERLY...
