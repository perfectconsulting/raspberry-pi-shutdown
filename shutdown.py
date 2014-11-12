import thread
import RPi.GPIO as GPIO
import time
import os

CONST_LED_PIN = 12;
CONST_SWITCH_PIN = 26;

led_state = 0
led_action = "off";

GPIO.setwarnings(False);

def led(debug):
    while led_action != "stop":
        if debug: print led_action; 
        if led_action == "off":   
            GPIO.output(CONST_LED_PIN, 0);        
        elif led_action == "on":       
            GPIO.output(CONST_LED_PIN, 1);
        elif led_action ==  "slowflash":
            GPIO.output(CONST_LED_PIN,1);
            time.sleep(2);
            GPIO.output(CONST_LED_PIN,0);
            time.sleep(2);
        elif led_action == "fastflash":
            GPIO.output(CONST_LED_PIN,1);
            time.sleep(0.1);
            GPIO.output(CONST_LED_PIN,0);
            time.sleep(0.1);

   
GPIO.cleanup();
GPIO.setmode(GPIO.BOARD)

GPIO.setup(CONST_LED_PIN,GPIO.OUT)
GPIO.setup(CONST_SWITCH_PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

thread.start_new_thread(led, (False,)); 
led_action="on";

try:
    while True:
        if  GPIO.input(CONST_SWITCH_PIN):
            led_action="fastflash";
            print "shutting down now";
            time.sleep(2);
            os.system("sudo shutdown -hP now");

except KeyboardInterrupt:
	GPIO.cleanup();
