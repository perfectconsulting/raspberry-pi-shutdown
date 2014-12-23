# Copyright 2011-2013 S J Consulting Ltd. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0.html
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

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
