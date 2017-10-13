from FlowChecker import FlowChecker
from csv import DictReader

class ChartGenerate:

    flowManager = None
    directPacketsTime = {}

    def __init__(self, directFlowPath, reverseFlowPath):

        self.flowManager = FlowChecker(directFlowPath, reverseFlowPath)
        if self.flowManager == None:
            return

        directFlowDict = DictReader(open(directFlowPath))
        for packets in directFlowDict:
            self.directPacketsTime.update({packets['Frame']:packets['Time']})

    def makeChart(self, tuples, xLabel, yLabel, chartType):

        header = "\\documentclass{standalone}\n" + "\\usepackage{tikz}\n" + "\\usepackage{pgfplots}\n\n" + "\\begin{document}\n" + "\\begin{tikzpicture}\n" + "    \\begin{axis}[\n"
        axis = "        xlabel=$" + xLabel + "$,\n" + "        ylabel=$" + yLabel + "$]\n"
        plotDefs = "    	\\addplot[smooth,mark=*,blue] plot coordinates {\n"
        plots = ""
        for tuple in tuples:
            if chartType == 1:
                plots += "        	(" + str(tuple[0]) + "," + str(float("{0:.10f}".format(tuple[1] * 1000))) + ")\n"
            else:
                plots += "        	(" + str(tuple[0]) + "," + str(tuple[1]) + ")\n"
        endind = "    	};\n" + "    \end{axis}\n" + "    \end{tikzpicture}\n" + "\end{document}"

        return header + axis + plotDefs + plots + endind

    def makeChartBody(self, tuples, xLabel, yLabel, chartType):

        header = "\\begin{tikzpicture}\n" + "    \\begin{axis}[\n"
        axis = "        xlabel=$" + xLabel + "$,\n" + "        ylabel=$" + yLabel + "$]\n"
        plotDefs = "    	\\addplot[smooth,mark=*,blue] plot coordinates {\n"
        plots = ""
        for tuple in tuples:
            if chartType == 1:
                plots += "        	(" + str(tuple[0]) + "," + str(float("{0:.10f}".format(tuple[1] * 1000))) + ")\n"
            else:
                plots += "        	(" + str(tuple[0]) + "," + str(tuple[1]) + ")\n"
        endind = "    	};\n" + "    \end{axis}\n" + "    \end{tikzpicture}\n"

        return header + axis + plotDefs + plots + endind

    def makeChartDocument(self, body):

        header = "\\documentclass{standalone}\n" + "\\usepackage{tikz}\n" + "\\usepackage{pgfplots}\n\n" + "\\begin{document}\n"
        endind = "\end{document}"

        return header + body + endind

    def getRTTChart(self, chartPath):

        rtt = sorted(self.flowManager.getRTT().items(), key = lambda frame : int(frame[0]))
        chart = self.makeChart(rtt, "Packets", "RTT(ms)", 1)
        chartFile = open(chartPath, 'w')
        chartFile.write(chart)

    def getJitterChart(self, chartPath):

        rtt = self.flowManager.getRTT()
        jitter = sorted(self.flowManager.getJitter(rtt).items(), key = lambda frame : int(frame[0]))
        chart = self.makeChart(jitter, "Packets", "Jitter(ms)", 1)
        chartFile = open(chartPath, 'w')
        chartFile.write(chart)

    def getPPSChart(self, chartPath):

        pps = sorted(self.flowManager.getPPS().items(), key = lambda frame : int(frame[0]))
        chart = self.makeChart(pps, "Time(s)", "PPS", 2)
        chartFile = open(chartPath, 'w')
        chartFile.write(chart)

    def getThroughputChart(self, chartPath):

        throughput = sorted(self.flowManager.getThroughput().items(), key = lambda frame : int(frame[0]))
        chart = self.makeChart(throughput, "Time(s)", "Throughput(B/s)", 2)
        chartFile = open(chartPath, 'w')
        chartFile.write(chart)

    def getErrorsChart(self, chartPath):

        errors = sorted(self.flowManager.getErrors().items(), key = lambda frame : int(frame[0]))
        chart = self.makeChart(errors, "Time(s)", "Errors", 2)
        chartFile = open(chartPath, 'w')
        chartFile.write(chart)

    def getFullAnalysis(self, chartPath):

        rttData = self.flowManager.getRTT()
        rtt = sorted(rttData.items(), key=lambda frame: int(frame[0]))
        chart = self.makeChartBody(rtt, "Packets", "RTT(ms)", 1) + "\n"
        jitter = sorted(self.flowManager.getJitter(rttData).items(), key=lambda frame: int(frame[0]))
        chart += self.makeChartBody(jitter, "Packets", "Jitter(ms)", 1) + "\n"
        pps = sorted(self.flowManager.getPPS().items(), key=lambda frame: int(frame[0]))
        chart += self.makeChartBody(pps, "Time(s)", "PPS", 2) + "\n"
        throughput = sorted(self.flowManager.getThroughput().items(), key=lambda frame: int(frame[0]))
        chart += self.makeChartBody(throughput, "Time(s)", "Throughput(B/s)", 2) + "\n"
        errors = sorted(self.flowManager.getErrors().items(), key=lambda frame: int(frame[0]))
        chart += self.makeChartBody(errors, "Time(s)", "Errors", 2)

        chart = self.makeChartDocument(chart)
        chartFile = open(chartPath, 'w')
        chartFile.write(chart)
