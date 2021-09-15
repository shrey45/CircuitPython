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
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.


## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

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
