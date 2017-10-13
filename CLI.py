from ChartGenerate import ChartGenerate
from CSVFragment import CSVFragment

class CLI:
    CSV = CSVFragment()
    CHART = None

    LOADEDFLOWS = None

    def separateFlows(self, filePath):

        self.LOADEDFLOWS = self.CSV.getServiceFlows(filePath)
        if isinstance(self.LOADEDFLOWS, list):
            return 0
        else:
            return -1

    def readFlows(self, directoryPath):

        self.LOADEDFLOWS = self.CSV.readServiceFlows(directoryPath)
        if isinstance(self.LOADEDFLOWS, list):
            return 0
        else:
            return -1

    def showFlows(self):

        if self.LOADEDFLOWS == None:
            return -1
        else:
            for flow in self.LOADEDFLOWS[0]:
                print flow

    def persistFlows(self, persistLocal):

        if self.LOADEDFLOWS == None:
            return -1
        else:
            self.CSV.persistServiceFlows(self.LOADEDFLOWS, persistLocal)

    def unifyFlows(self, directoryPath, flowsID):

        return self.CSV.unifyFlowsTraffic(directoryPath, flowsID)

    def loadChartModule(self, directFlow, reverseFlow):

        self.CHART = ChartGenerate(directFlow, reverseFlow)
        if self.CHART.flowManager == None:
            return -1
        else:
            return 0

    def CLIMain(self):

        ONOFF = True
        while (ONOFF):
            if self.CHART == None:
                print '\n------------- MENU -------------'
                print '0- EXIT'
                print '1- FLOWS CSV MANIPULATION'
                print '2- CHARGE FLOW CHECKER MODULE'
                print '--------------------------------'
                Option = raw_input('OPTION: ')

                if Option == '0':
                    ONOFF = False
                    continue
                if Option == '1':
                    while Option != '0':
                        print '\n------------- MENU -------------'
                        print '0- BACK'
                        print '1- SEPARATE FLOWS FROM CSV'
                        print '2- READ SEPARATED FLOWS FROM DIRECTORY'
                        print '3- SHOW READ FLOWS'
                        print '4- PERSIST LOADED FLOWS'
                        print '5- UNIFY FLOW FILES'
                        print '--------------------------------'
                        Option = raw_input('OPTION: ')

                        if Option == '0':
                            self.LOADEDFLOWS = None
                            continue
                        if Option == '1':
                            Data = raw_input('CSV FLOW FILE PATH: ')
                            Result = self.separateFlows(Data)
                            if Result == -1:
                                print 'CAN NOT LOAD FILE!!'
                            else:
                                print 'SUCCESS!!'
                        if Option == '2':
                            Data = raw_input('SEPARETED FLOWS DIRECTORY PATH: ')
                            Result = self.readFlows(Data)
                            if Result == -1:
                                print 'CAN NOT LOAD FLOWS!!'
                            else:
                                print 'SUCCESS!!'
                        if Option == '3':
                            Result = self.showFlows()
                            if Result == -1:
                                print 'FLOWS UNLOADED!!\n'
                        if Option == '4':
                            Data = raw_input('PERSIST LOCAL: ')
                            Result = self.persistFlows(Data)
                            if Result == -1:
                                print 'CAN NOT PERSIST FLOWS!!\n'
                            else:
                                print 'SUCCESS!!\n'
                        if Option == '5':
                            Data = raw_input('CSV FLOW FOLDER PATH: ')
                            FirstFile = raw_input('FIRST FLOW ID: ')
                            SecondFile = raw_input('SECOND FLOW ID: ')
                            Result = self.unifyFlows(Data, [FirstFile, SecondFile])
                            if Result == -1:
                                print 'CAN NOT UNIFY FLOW FILES!!\n'
                            else:
                                print 'SUCCESS!!\n'

                if Option == '2':
                    Direct = raw_input('DIRECT FLOW FILE PATH: ')
                    Reverse = raw_input('REVERSE FLOW FILE PATH: ')
                    Result = self.loadChartModule(Direct, Reverse)
                    if Result == -1:
                        print 'CAN NOT LOAD FLOW FILES!!\n'
                    else:
                        while Option != '0':
                            print '0- BACK'
                            print '1- GENERATE RTT CHART'
                            print '2- GENERATE JITTER CHART'
                            print '3- GENERATE PPS CHART'
                            print '4- GENERATE THROUGHPUT CHART'
                            print '5- GENERATE ERRORS CHART'
                            print '6- GENERATE FULL ANALYSIS CHART'
                            Option = raw_input('OPTION: ')

                            if Option == '0':
                                self.CHART = None
                                continue
                            if Option == '1':
                                Data = raw_input('RTT CHART PATH AND NAME: ')
                                self.CHART.getRTTChart(Data)
                                print 'SUCCESS!!\n'
                            if Option == '2':
                                Data = raw_input('JITTER CHART PATH AND NAME: ')
                                self.CHART.getJitterChart(Data)
                                print 'SUCCESS!!\n'
                            if Option == '3':
                                Data = raw_input('PPS CHART PATH AND NAME: ')
                                self.CHART.getPPSChart(Data)
                                print 'SUCCESS!!\n'
                            if Option == '4':
                                Data = raw_input('THOROUGHPUT CHART PATH AND NAME: ')
                                self.CHART.getThroughputChart(Data)
                                print 'SUCCESS!!\n'
                            if Option == '5':
                                Data = raw_input('ERRORS CHART PATH AND NAME: ')
                                self.CHART.getErrorsChart(Data)
                                print 'SUCCESS!!\n'
                            if Option == '6':
                                Data = raw_input('FULL CHART PATH AND NAME: ')
                                self.CHART.getFullAnalysis(Data)
                                print 'SUCCESS!!\n'

MAIN = CLI()
MAIN.CLIMain()