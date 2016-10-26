# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:40:58 2016

@author: 502677886
"""


class InputOilParameters:

    def __init__(self, pad, wp, averageHeight, averagePorosity,
                 averageOilSaturation, averageDrainageArea, averageWellLength,
                 residualOilSaturation, residualAngle):

        # input parameters
        self.padName = pad
        self.wellPairs = wp
        self.averageProdHeight = averageHeight
        self.averagePorosity = averagePorosity
        self.averageOilSaturation = averageOilSaturation
        self.averageDrainageArea = averageDrainageArea  # m2
        self.averageWellLength = averageWellLength  # m
        self.residualOilSaturation = residualOilSaturation
        self.residualAngle = residualAngle

    def getPadname(self):
        return(self.padName)

    def setPadName(self, pad):
        self.padName = pad

    def getWellPairs(self):
        return(self.wellPairs)

    def setWellPairs(self, wp):
        self.wellPairs = wp

    def getAverageProdHeight(self):
        return(self.averageProdHeight)

    def setAverageProdHeight(self, averageHeight):
        self.averageProdHeight = averageHeight

    def getAveragePorosity(self):
        return(self.averagePorosity)

    def setAveragePorosity(self, averagePorosity):
        self.averagePorosity = averagePorosity

    def getAverageOilSaturation(self):
        return(self.averageOilSaturation)

    def setAverageOilSaturation(self, averageOilSaturation):
        self.averageOilSaturation = averageOilSaturation

    def getAverageDrainageArea(self):
        return(self.averageDrainageArea)

    def setAverageDrainageArea(self, averageDrainageArea):
        self.averageDrainageArea = averageDrainageArea

    def getAverageWellLength(self):
        return(self.averageWellLength)

    def setAverageWellLength(self, averageWellLength):
        self.averageWellLength = averageWellLength

    def getResidualOilSaturation(self):
        return(self.residualOilSaturation)

    def setResidualOilSaturation(self, residualOilSaturation):
        self.residualOilSaturation = residualOilSaturation

    def getResidualAngle(self):
        return(self.residualAngle)

    def setResidualAngle(self, residualAngle):
        self.residualAngle = residualAngle

    #  Δ Oil Saturation (Soi - Sor)
    def deltaOilSaturation(self):
        delta = self.averageOilSaturation - self.residualOilSaturation
        return(delta)
