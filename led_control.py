#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
import sys

# Configuration des broches GPIO
G = 18
B = 19
R = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

# Initialisation des broches PWM
R_pin = GPIO.PWM(R, 100)
G_pin = GPIO.PWM(G, 100)
B_pin = GPIO.PWM(B, 100)

# Récupération des valeurs de couleur depuis les arguments en ligne de commande
R_color = int(sys.argv[1])
G_color = int(sys.argv[2])
B_color = int(sys.argv[3])

# Affichage de la valeur de la broche R (peut être supprimé si vous n'en avez pas besoin)
print(int(R_color * 100 // 255))

# Démarrage des broches PWM
R_pin.start(50)
G_pin.start(0)
B_pin.start(0)

# Réglage des cycles de service pour chaque couleur
R_pin.ChangeDutyCycle(R_color * 100 // 256)
G_pin.ChangeDutyCycle(G_color * 100 // 256)
B_pin.ChangeDutyCycle(B_color * 100 // 256)


print(f'RGB = ({R_color}, {G_color}, {B_color})')
# Attente pendant 5 secondes (vous pouvez ajuster cette durée selon vos besoins)
time.sleep(5)

# Arrêt des broches PWM
R_pin.stop()
G_pin.stop()
B_pin.stop()

GPIO.cleanup()
