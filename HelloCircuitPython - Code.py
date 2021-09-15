import time
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
x = 25
y = 25
z = 25

while True:

dot.fill((x, y, z,))
time.sleep(1)
x = x+1
if x>=255:
    x = 20

y = y+5
if y>=255:
    y = 20

z = z+10
if z>=255:
    z = 20

print(x,y,x)