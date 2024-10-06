#!/usr/bin/python3
import RPi.GPIO as GPIO
import sys


# Configuration du GPIO
LED_PIN = 4  # Numéro du pin GPIO où la LED est connectée

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Allumer ou éteindre la LED
if len(sys.argv) != 2:
    print("Usage: python3 led_control.py <on|off>")
    sys.exit(1)

command = sys.argv[1].lower()
if command == "on":
    print('on')
    GPIO.output(LED_PIN, GPIO.HIGH)
elif command == "off":
    GPIO.output(LED_PIN, GPIO.LOW)
    print('off')
else:
    print("Commande non reconnue. Utilisez 'on' ou 'off'.")
    sys.exit(1)