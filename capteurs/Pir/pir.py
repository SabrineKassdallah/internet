import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN) #PIR
GPIO.setup(5, GPIO.OUT) #BUzzer

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(6):
            GPIO.output(5, True)
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            GPIO.output(5, False)
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()
