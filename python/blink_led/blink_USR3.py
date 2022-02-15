import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("USR3", GPIO.OUT)

pin = "USR3"

while (1==1):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(.1)