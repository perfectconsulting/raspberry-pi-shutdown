raspberry-pi-shutdown
=====================

A simple shutdown button for the Raspberry Pi. The script will turn the led on to indicate that the script is running correctly.When you press the shutdown button. the light will start to flash quickly until the Raspberry Pi shutsdown.

Setup
=====

1. copy the scripts to a local folder on the pi (in this case /home/pi)
2. add the following entry to crontab **@reboot sudo /home/pi/shutdown.sh**
3. restart the Raspberry Pi

![circuit](https://cloud.githubusercontent.com/assets/8858414/5050038/aed6d102-6c22-11e4-9178-1cc8cb32a057.png "Circuit")
