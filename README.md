# CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
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
[Click Here for the Full Code](https://github.com/shrey45/CircuitPython/blob/main/Code/CircuitPython_Servo.py)

### Evidence

https://user-images.githubusercontent.com/63983735/133453060-47586578-9ce4-4183-98fa-976e8902bab3.mp4

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
