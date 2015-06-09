import RPi.GPIO as GPIO
import time

# use Raspberry Pi GPIO numbers, and assign pins to each place in the binary counter
GPIO.setmode(GPIO.BCM)

onesPlace = 26
twosPlace = 6
foursPlace = 22
eightsPlace = 17

# LED lighting function
def lightme(string):
	GPIO.setmode(GPIO.BCM)
	a = string[-1:]		# check the ones place
	b = string[-2:-1]	# check the twos place
	c = string[-3:-2]	# check the fours place
	d = string[-4:-3]	# check the eights place
	if(a == "1"):
		GPIO.setup(onesPlace,GPIO.OUT)
		GPIO.output(onesPlace,GPIO.HIGH)
	if(b == "1"):
		GPIO.setup(twosPlace,GPIO.OUT)
		GPIO.output(twosPlace,GPIO.HIGH)
	if(c == "1"):
		GPIO.setup(foursPlace,GPIO.OUT)
		GPIO.output(foursPlace,GPIO.HIGH)
	if(d == "1"):
		GPIO.setup(eightsPlace,GPIO.OUT)
		GPIO.output(eightsPlace,GPIO.HIGH)
	# keep LEDS lit for 1 second, then turn off all LEDs
	time.sleep(1)
	GPIO.setup(onesPlace,GPIO.OUT)
	GPIO.output(onesPlace,GPIO.LOW)
	GPIO.setup(twosPlace,GPIO.OUT)
	GPIO.output(twosPlace,GPIO.LOW)
	GPIO.setup(foursPlace,GPIO.OUT)
	GPIO.output(foursPlace,GPIO.LOW)
	GPIO.setup(eightsPlace,GPIO.OUT)
	GPIO.output(eightsPlace,GPIO.LOW)
	return

for x in range(1,16):
	binnum = bin(x)[2:]	# set everything after the "0b" to binnum, then feed that to the function to light the appropriate LEDs
	lightme(binnum)

GPIO.cleanup()