#!/bin/bash

python ./LaundryMachineSensor.py -r /Users/fbleite/Development/iotPlayground/root-CA.crt \
                                -c /Users/fbleite/Development/iotPlayground/MacbookPro.cert.pem \
                                -k /Users/fbleite/Development/iotPlayground/MacbookPro.private.key \
                                -id MacbookPro
                                -t 1500