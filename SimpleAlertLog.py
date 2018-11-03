

class SimpleAlertLog :
    def alertMachineStatusChanged (self, isMachineTurnedOn):
        if isMachineTurnedOn:
            print('Machine turned on')
        else :
            print('Machine turned off')