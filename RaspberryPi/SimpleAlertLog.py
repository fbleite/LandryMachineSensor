import logging

class SimpleAlertLog :
    def alertCurrentStatus(self, laundryMachineStatus):
        logging.info(laundryMachineStatus.generateAlertMessage())
