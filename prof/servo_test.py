#!/usr/bin/env python
import PCA9685 as servo
import time                  # Import necessary modules

MinPulse = 50
MidPulse = 250
MaxPulse = 450

def setup():
    global pwm
    pwm = servo.PWM()
    pwm.frequency = 50

def servo_test():
    while True:
        for value in range(MinPulse, MaxPulse, 25):
            print ('PWM value: %d' % value)
            pwm.write(0, 0, value)
            time.sleep(0.05)
    
        for value in range(MaxPulse, MinPulse, -25):
            print ('PWM value: %d' % value)
            pwm.write(0, 0, value)
            time.sleep(0.05)

if __name__ == '__main__':
    setup()
    servo_test()