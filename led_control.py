#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

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

# Démarrage des broches PWM
R_pin.start(0)
G_pin.start(0)
B_pin.start(0)

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        color = json.loads(post_data)
        
        R_color = color['R']
        G_color = color['G']
        B_color = color['B']

        # Réglage des cycles de service pour chaque couleur
        R_pin.ChangeDutyCycle(R_color * 100 // 256)
        G_pin.ChangeDutyCycle(G_color * 100 // 256)
        B_pin.ChangeDutyCycle(B_color * 100 // 256)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Color changed')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

try:
    run()
except KeyboardInterrupt:
    R_pin.stop()
    G_pin.stop()
    B_pin.stop()
    GPIO.cleanup()
