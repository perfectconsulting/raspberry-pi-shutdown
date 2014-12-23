import thread
import RPi.GPIO as GPIO
import os
import time

CONST_LED_PIN = 12;
CONST_SWITCH_PIN = 26;

GPIO.setwarnings(False);
   
GPIO.cleanup();
GPIO.setmode(GPIO.BOARD)

GPIO.setup(CONST_LED_PIN,GPIO.OUT)
GPIO.setup(CONST_SWITCH_PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:

    GPIO.output(CONST_LED_PIN,1);
    
    while not GPIO.input(CONST_SWITCH_PIN):
        time.sleep(0.1);
 
    os.system("sudo shutdown -hP now");

    while True:
            GPIO.output(CONST_LED_PIN,1);
            time.sleep(0.1);
            GPIO.output(CONST_LED_PIN,0);
            time.sleep(0.1);

except KeyboardInterrupt:
	GPIO.cleanup();
