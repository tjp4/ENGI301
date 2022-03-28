import stepper.mpy
import Adafruit_BBIO.GPIO as GPIO
import time
import math



DELAY = 0.01
STEPS = 200

pin=["P1_2", "P1_4", "P1_6", "P1_8"]
GPIO.setup(pin[0], GPIO.OUT)
GPIO.setup(pin[1], GPIO.OUT)
GPIO.setup(pin[2], GPIO.OUT)
GPIO.setup(pin[3], GPIO.OUT)

coils = pin

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

for step in range(STEPS):
    motor.onestep()
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(direction=stepper.BACKWARD)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(style=stepper.DOUBLE)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(style=stepper.INTERLEAVE)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    time.sleep(DELAY)

motor.release()