import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

print "Start LED"

i = 0
while i < 10:
	GPIO.output(21, False)
	time.sleep(1)
	GPIO.output(21, True)
	time.sleep(1)
	i +=1

print "End LED"

GPIO.cleanup()
