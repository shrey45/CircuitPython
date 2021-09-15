import time
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
x = 50
y = 50
z = 50

while True:

dot.fill((x, y, z,))
time.sleep(.5)
x = x+5
if x==255:
    x = 10

y = y+1
if y==255:
    y = 10

z = z*2
if z>255:
    z = 10