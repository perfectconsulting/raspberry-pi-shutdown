

/*
 * Copyright 2011-2013 S J Consulting Ltd. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"). You
 *  may not use this file except in compliance with the License. A copy of
 * the License is located at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0.html
 *
 * or in the "license" file accompanying this file. This file is
 * distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
 * ANY KIND, either express or implied. See the License for the specific
 * language governing permissions and limitations under the License.
 */

#include <stdio.h>
#include <wiringPi.h>

const int butPin = 22;

int main(void)
{
    wiringPiSetupGpio();
    pinMode(butPin, INPUT);
    pullUpDnControl(butPin, PUD_DOWN);

    while(!digitalRead(butPin))
    {
      delay(500);
    }

    printf("shutting down now!\n");
    system("sudo shutdown -hP now");
}

