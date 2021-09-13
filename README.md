# Circuit Python

## Intro to Circuit Python

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
