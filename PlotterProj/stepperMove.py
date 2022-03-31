
import time
import board
import digitalio
import pwmio
from adafruit_motor import stepper
import kinematics

import Adafruit_BBIO.PWM as PWM

servo_pin = "P1_36"
duty_min = 5
duty_max = 10
duty_span = duty_max - duty_min

PWM.start(servo_pin, (100-duty_min), 50.0)

#200 steps = 360DEG
#1.8 degrees per step
#1 RPM = 360 deg/min = 60 deg/sec = 33.333 step/sec
coils = (
    digitalio.DigitalInOut(board.P2_2),  # A1
    digitalio.DigitalInOut(board.P2_4),  # A2
    digitalio.DigitalInOut(board.P2_6),  # B1
    digitalio.DigitalInOut(board.P2_8),  # B2
    digitalio.DigitalInOut(board.P2_18),  # A1
    digitalio.DigitalInOut(board.P2_20),  # A2
    digitalio.DigitalInOut(board.P2_22),  # B1
    digitalio.DigitalInOut(board.P2_24),  # B2
)


for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

motor1 = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)
motor2 = stepper.StepperMotor(coils[4], coils[5], coils[6], coils[7], microsteps=None)

def zero():
    motor1.release()
    motor2.release()
    wait = input("zero arm now")
    print("arm zeroed")

def m1(curr,new,spd):
    th = new - curr
    STEPS = abs(kinematics.deg2step(th))
    DELAY = 1/(33.3*spd)    #spd in rpm
    if (th<0):
        for step in range(STEPS):
            motor1.onestep()
            time.sleep(DELAY)
    elif (th>0):
        for step in range(STEPS):
            motor1.onestep(direction=stepper.BACKWARD)
            time.sleep(DELAY)

def m2(curr,new,spd):
    th = new - curr
    STEPS = abs(kinematics.deg2step(th))
    DELAY = 1/(33.3*spd)    #spd in rpm

    if (th<0):
        for step in range(STEPS):
            motor2.onestep()
            time.sleep(DELAY)
    elif (th>0):
        for step in range(STEPS):
            motor2.onestep(direction=stepper.BACKWARD)
            time.sleep(DELAY)

def pen(a):
    if(a>0):
        angle_f = float(0)
        duty = 100 - ((angle_f / 180) * duty_span + duty_min) 
        print(duty)
        PWM.set_duty_cycle(servo_pin, duty)
    else:
        angle_f = float(90)
        duty = 100 - ((angle_f / 180) * duty_span + duty_min) 
        print(duty)
        PWM.set_duty_cycle(servo_pin, duty)
        
