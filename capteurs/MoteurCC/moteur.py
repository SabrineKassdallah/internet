#!/usr/bin/python
#i2c 0x60 0x70

from Adafruit_MotorHAT import Adafruit_MotorHAT,Adafruit_DCMotor

import time
import atexit

mh=Adafruit_MotorHAT(addr=0x60)
MAX_SPEED=150

def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

motor=mh.getMotor(1)

while True:
	print("Forward \n")
	motor.run(Adafruit_MotorHAT.FORWARD)
	print("Speed up \n")
	for i in range(MAX_SPEED):
		motor.setSpeed(i)
		time.sleep(0.01)
	
	print("Speed down \n")
	for i in reversed(range(MAX_SPEED)):
		motor.setSpeed(i)
		time.sleep(0.01)
	
	print("Backward\n")
	motor.run(Adafruit_MotorHAT.BACKWARD)
	print "Speed up \n"
	for i in range(MAX_SPEED):
		motor.setSpeed(i)
		time.sleep(0.01)
	
	print("Speed down \n")
	for i in reversed(range(MAX_SPEED)):
		motor.setSpeed(i)
		time.sleep(0.01)
	
	print("STOP \n")
	motor.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(2)
