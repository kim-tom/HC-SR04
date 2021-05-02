from wsgiref.simple_server import make_server
import RPi.GPIO as GPIO
import time
import json

TRIG = 3
ECHO = 4
LED = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def get_distance():
  GPIO.output(TRIG, GPIO.LOW)
  time.sleep(0.3)
  GPIO.output(LED, GPIO.HIGH)
  GPIO.output(TRIG, GPIO.HIGH)
  time.sleep(0.00001)
  GPIO.output(TRIG, GPIO.LOW)
  while GPIO.input(ECHO) == 0:
    signaloff = time.perf_counter()
  while GPIO.input(ECHO) == 1:
    signalon = time.perf_counter()
  GPIO.output(LED, GPIO.LOW)
  timepassed = signalon - signaloff
  distance = timepassed * 17150
  return int(distance)
def app(environ, start_response):
  status = '200 OK'
  headers = [
    ('Content-type', 'application/json; charset=utf-8'),
    ('Access-Control-Allow-Origin', '*'),
  ]
  start_response(status, headers)
  return [json.dumps({'distance': get_distance()}).encode("utf-8")]

with make_server('', 3003, app) as httpd:
  print("Serving on port 3003...")
  httpd.serve_forever()
