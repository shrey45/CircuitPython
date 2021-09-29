"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import servo
import touchio

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

touch_pad = board.A4
touch1_pad = board.A5

touch = touchio.TouchIn(touch_pad)
touch1 = touchio.TouchIn(touch1_pad)

while True:
    if touch.value:
        my_servo.angle = 180
        time.sleep(0.05)
    if touch1.value:
        my_servo.angle = 0
        time.sleep(0.05)