import logging

class SimpleAlertLog :
    def alertMachineStatusChanged (self, isMachineTurnedOn):
        if isMachineTurnedOn:
            logging.info('Machine turned on')
        else :
            logging.info('Machine turned off')

    # def alertCurrentStatus(self, ):