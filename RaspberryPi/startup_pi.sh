#!/bin/bash

python ./LaundryMachineSensor.py -r /home/pi/laundryMachineSensor/iotConnection/root-CA.crt \
                                -c /home/pi/laundryMachineSensor/iotConnection/RaspberryPi.cert.pem \
                                -k /home/pi/laundryMachineSensor/iotConnection/RaspberryPi.private.key \
                                -id RaspberryPi \
                                -t 1500