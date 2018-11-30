#!/bin/bash

/home/pi/laundryMachineSensor/venv/bin/python /home/pi/laundryMachineSensor/LandryMachineSensor/RaspberryPi/LaundryMachineSensor.py \
                                -r /home/pi/laundryMachineSensor/iotConnection/root-CA.crt \
                                -c /home/pi/laundryMachineSensor/iotConnection/RaspberryPi.cert.pem \
                                -k /home/pi/laundryMachineSensor/iotConnection/RaspberryPi.private.key \
                                -id RaspberryPi \
                                -t 11 \
                                -l /home/pi/laundryMachineSensor/sensor.log
