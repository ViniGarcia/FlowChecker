from csv import DictReader, DictWriter
from os.path import isfile, isdir
from os import mkdir, listdir

class CSVFragment:

    def getServiceFlows(self, csvFilePath):

        if not isfile(csvFilePath):
            return

        csvFile = open(csvFilePath)
        csvDict = DictReader(csvFile)

        #{Src, Dst, SrcPort, DstPort, Serv}
        flowsList = []
        #[Packets]
        flowsPackets = []

        for packet in csvDict:
            flow = {'Src':packet['Source'], 'Dst':packet['Destination'], 'SrcPort':packet['SrcPort'], 'DstPort':packet['DstPort'], 'Serv':packet['Protocol']}

            if flow not in flowsList:
                flowsList.append(flow)
                flowsPackets.append([])

            flowID = flowsList.index(flow)
            flowsPackets[flowID].append(packet)

        return [flowsList, flowsPackets]


    def persistServiceFlows(self, flowsData):

        if not isdir('Result'):
            mkdir('Result')
        flowInfo = open('Result/1.InfoFile.txt', 'w')
        packetHeader = ['Time','Source','Destination','SrcPort','DstPort','Protocol','Frame','Ack','Bytes','Payload']

        for flow in flowsData[0]:
            flowInfo.write("ID: " + str(flowsData[0].index(flow)) + "\nSource: " + str(flow['Src']))
            flowInfo.write("\nDestiny: " + str(flow['Dst']) + "\nSrcPort: " + str(flow['SrcPort']))
            flowInfo.write("\nDstPort: " + str(flow['DstPort']) + "\nService: " + str(flow['Serv']) + "\n\n")

            packetsInfo = open("Result/" + str(flowsData[0].index(flow)) + ".txt", 'w')
            packetsWriter = DictWriter(packetsInfo, packetHeader, delimiter=',')
            packetsWriter.writeheader()
            for packet in flowsData[1][flowsData[0].index(flow)]:
                packetsWriter.writerow(packet)

    def readServiceFlows(self, flowsFolder):

        if not isdir(flowsFolder):
            return

        flowsList = []
        flowsPackets = []

        folder = listdir(flowsFolder)
        for fileName in range(0, len(folder)-1):
            csvFile = open(flowsFolder + "/" + str(fileName) + ".txt")
            csvDict = DictReader(csvFile)

            packets = []
            for packet in csvDict:
                packets.append(packet)
            flow = {'Src': packet['Source'], 'Dst': packet['Destination'], 'SrcPort': packet['SrcPort'], 'DstPort': packet['DstPort'], 'Serv': packet['Protocol']}
            flowsList.append(flow)
            flowsPackets.append(packets)

        return [flowsList, flowsPackets]

    def unifyFlowsTraffic(self, flowsFolder, flowsNumber):

        if not isdir(flowsFolder):
            return

        resultFile = ""
        resultDict = []

        for flow in flowsNumber:
            filePath = flowsFolder + '/' + flow + '.txt'
            if isfile(filePath):
                resultFile += flow + '_'
                csvFile = open(filePath)
                resultDict.append(DictReader(csvFile))
        resultFile += '.txt'

        packetHeader = ['Time', 'Source', 'Destination', 'SrcPort', 'DstPort', 'Protocol', 'Frame', 'Ack', 'Bytes', 'Payload']
        packetsInfo = open(resultFile, 'w')
        packetsWriter = DictWriter(packetsInfo, packetHeader, delimiter=',')
        packetsWriter.writeheader()
        packetsList = []
        for packetSet in resultDict:
            for packet in packetSet:
                packetsList.append(packet)
        packetsList = sorted(packetsList, key=lambda k: k['Time'])
        for packet in packetsList:
            packetsWriter.writerow(packet)

lala = CSVFragment()
data = lala.getServiceFlows('FlowTest.csv')
lala.persistServiceFlows(data)
lala.readServiceFlows('Result')
lala.unifyFlowsTraffic('Result', ['5','7'])