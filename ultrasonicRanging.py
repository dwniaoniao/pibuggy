import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig = 2
echo = 3

GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def ranging():
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)
    
    while GPIO.input(echo) == GPIO.LOW:
        pass
    
    echoPulseStart = time.time()
    
    while GPIO.input(echo) == GPIO.HIGH:
        pass 
    
    echoPulseEnd = time.time()
    echoPulseDuration = echoPulseEnd - echoPulseStart
    distance = echoPulseDuration * 340 / 2 * 100
    return distance

if __name__ == "__main__":
    try:
        while True:
            d = ranging()
            print("Distance = %fcm"%d)
    except KeyboardInterrupt:
        GPIO.cleanup()
