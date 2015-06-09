import RPi.GPIO as GPIO
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# blinking function
def lightme(string):
	GPIO.setmode(GPIO.BCM)
	a = string[-1:]
	b = string[-2:-1]
	c = string[-3:-2]
	d = string[-4:-3]
	if(a == "1"):
		GPIO.setup(26,GPIO.OUT)
		GPIO.output(26,GPIO.HIGH)
	if(b == "1"):
		GPIO.setup(6,GPIO.OUT)
		GPIO.output(6,GPIO.HIGH)
	if(c == "1"):
		GPIO.setup(22,GPIO.OUT)
		GPIO.output(22,GPIO.HIGH)
	if(d == "1"):
		GPIO.setup(17,GPIO.OUT)
		GPIO.output(17,GPIO.HIGH)
	time.sleep(1)
	GPIO.setup(26,GPIO.OUT)
	GPIO.output(26,GPIO.LOW)
	GPIO.setup(6,GPIO.OUT)
	GPIO.output(6,GPIO.LOW)
	GPIO.setup(22,GPIO.OUT)
	GPIO.output(22,GPIO.LOW)
	GPIO.setup(17,GPIO.OUT)
	GPIO.output(17,GPIO.LOW)
	return

for x in range(1,16):
	binnum = bin(x)[2:]
	lightme(binnum)

GPIO.cleanup()
