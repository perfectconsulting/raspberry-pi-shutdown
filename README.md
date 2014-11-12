raspberry-pi-shutdown
=====================

A simple shutdown button for the Raspberry Pi. The script will turn the led on to indicate that the script is running correctly.When you press the shutdown button. the light will start to flash quickly until the Raspberry Pi shutsdown.

Installation
============

1. copy the scripts to a local folder on the pi (in this case /home/pi)
2. add the following entry to crontab **@reboot sudo /home/pi/shutdown.sh**
3. restart the Raspberry Pi

![Alt text](https://cloud.githubusercontent.com/assets/8858414/5014109/10ff3d22-6a8b-11e4-8eb2-f2dbd0075e47.png "Circuit")
