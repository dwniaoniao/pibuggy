import carControl
import ultrasonicRanging as ur 
from time import sleep
import RPi.GPIO as GPIO

speed = 40
turningSpeed = 50
turningDuration = 0.3
backwardDuration = 0.5

def slowDown():
    return speed - 10

def speedUp():
    s = speed + 10
    if s < 100:
        return s
    else:
        return 100

try:
    while True:
        carControl.forword(speed)
        print("forwording")
        if ur.ranging() < 20:
            carControl.stop()
            print("stop")
            sleep(0.5)
            carControl.backward(speed, backwardDuration)
            print("backwardding")
            carControl.stop()
            sleep(0.5)
            carControl.turnLeft(turningSpeed, turningDuration)
            print("turning left")
            carControl.stop()
            sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
