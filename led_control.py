#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
import sys


# Configuration du GPIO
G = 18
B = 19
R = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

R_pin = GPIO.PWM(R,100)
G_pin = GPIO.PWM(G,100)
B_pin = GPIO.PWM(B,100)


R_color = int(sys.argv[1])
G_color = int(sys.argv[2])
B_color = int(sys.argv[3])
print(int(R_color * 100 // 255))

R_pin.start(50)
G_pin.start(0)
B_pin.start(0)

try:
    while 1:
        R_pin.ChangeDutyCycle(R_color * 100 // 256)
        G_pin.ChangeDutyCycle(G_color * 100 // 256)
        B_pin.ChangeDutyCycle(B_color * 100 // 256)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
R_pin.stop()
G_pin.stop()
B_pin.stop()

GPIO.cleanup()

