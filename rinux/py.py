import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
LED = 11, 13, 15
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
try:
	while 1:
		swh = input()
		if swh == '1':
	     		GPIO.output(LED,GPIO.HIGH)
		else:
			GPIO.output(LED,GPIO.LOW)
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
