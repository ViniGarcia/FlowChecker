from csv import DictReader
from os.path import isfile
from copy import copy

class FlowChecker:

    directFlowFile = None
    reverseFlowFile = None

    def __init__(self, directFlow, reverseFlow):

        if not isfile(directFlow) or not isfile(reverseFlow):
            return

        self.directFlowFile = open(directFlow)
        self.reverseFlowFile = open(reverseFlow)


    def getRTT(self):

        self.directFlowFile.seek(0)
        self.reverseFlowFile.seek(0)
        directFlowDict = DictReader(self.directFlowFile)
        reverseFlowDict = DictReader(self.reverseFlowFile)

        rttData = {}
        for packets in directFlowDict:
            rttData.update({packets['Frame']:packets['Time']})

        for packets in reverseFlowDict:
            if packets['Ack'] != '':
                rttData[packets['Ack']] = float(packets['Time']) - float(rttData[packets['Ack']])

        rttIteration = copy(rttData)
        for data in rttIteration:
            if isinstance(rttIteration[data], basestring):
                rttData.pop(data)

        return rttData

    #def getJitter(self, rttData):

    def getThroughput(self):

        self.directFlowFile.seek(0)
        directFlowDict = sorted(DictReader(self.directFlowFile), key=lambda k: float(k['Time']))
        packetsPerSecond = {}
        currentTime = 1
        initialTime = None
        packetsAmount = 0

        for packet in directFlowDict:
            if initialTime == None:
                initialTime = float(packet['Time'])
            if float(packet['Time']) - initialTime >= 1:
                packetsPerSecond.update({currentTime: packetsAmount})
                initialTime = float(packet['Time'])
                currentTime += 1
                packetsAmount = 0
            packetsAmount += 1
        if packetsAmount > 0:
            packetsPerSecond.update({currentTime: packetsAmount})

        return packetsPerSecond

    def getErrors(self):

        self.directFlowFile.seek(0)
        directFlowDict = sorted(DictReader(self.directFlowFile), key=lambda k: float(k['Time']))
        errorsPerSecond = {}
        currentTime = 1
        initialTime = None
        errorsAmount = 0

        for packet in directFlowDict:
            if initialTime == None:
                initialTime = float(packet['Time'])
            if float(packet['Time']) - initialTime >= 1:
                errorsPerSecond.update({currentTime:errorsAmount})
                initialTime = float(packet['Time'])
                currentTime += 1
                errorsAmount = 0
            if packet['Payload'].startswith('['):
                errorsAmount += 1
        if errorsAmount > 0:
            errorsPerSecond.update({currentTime: errorsAmount})

        return errorsPerSecond

lala = FlowChecker('5_7_.txt', '6.txt')
print lala.getRTT()
print lala.getErrors()
print lala.getThroughput()