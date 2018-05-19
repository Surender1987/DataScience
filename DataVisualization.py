from matplotlib import pyplot as pit

""" 
***********************************************************************
Class to plot different type charts 
***********************************************************************
"""
class DataVisualization:
    xAxis = []
    yAxis = []
    title = ""
    yLabel = ""
    xLabel = ""

    def __init__(self, xAxis, yAxis, title, yLable, xLabel):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLable

    def DrawLineChart(self):
        pit.plot(self.xAxis, self.yAxis, color="Green", marker="o", linestyle="solid")
        pit.title(self.title)
        pit.ylabel(self.yLabel)
        pit.xlabel(self.xLabel)
        pit.show()

    def BarChart(self):
        pit.bar([x + 0.1 for x,_ in enumerate(self.yAxis)], self.yAxis)
        pit.xticks([x + 0.9 for x,_ in enumerate(self.xAxis)],self.xAxis)
        pit.title(self.title)
        pit.ylabel(self.yLabel)
        pit.xlabel(self.xLabel)
        pit.show()

