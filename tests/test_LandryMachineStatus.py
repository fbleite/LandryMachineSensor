from unittest import TestCase

from LaundryMachineStatus import LaundryMachineStatus

class test_LaundryMachineStatus(TestCase):
    def test_generateJsonStatus(self):
        lms = LaundryMachineStatus(threshold=1500)
        print(lms.generateJsonStatus())