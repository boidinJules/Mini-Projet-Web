import RPi.GPIO as GPIO
import sys

# Configuration du GPIO
LED_PIN = 18  # Numéro du pin GPIO où la LED est connectée
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Allumer ou éteindre la LED
if len(sys.argv) != 2:
    print("Usage: python3 led_control.py <on|off>")
    sys.exit(1)

command = sys.argv[1].lower()
if command == "on":
    GPIO.output(LED_PIN, GPIO.HIGH)
elif command == "off":
    GPIO.output(LED_PIN, GPIO.LOW)
else:
    print("Commande non reconnue. Utilisez 'on' ou 'off'.")
    sys.exit(1)

GPIO.cleanup()
