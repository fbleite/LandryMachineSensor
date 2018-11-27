import logging

class SimpleAlertLog :

    def __init__(self, args):
        pass

    def alertCurrentStatus(self, laundryMachineStatus):
        logging.info(laundryMachineStatus.generateAlertMessage())
