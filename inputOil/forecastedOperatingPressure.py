# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:34:19 2016

@author: 502677886
"""


class ForecastedOperatingPressure:

    def __init__(self, dateOfChange, operatingPressure):

        # forecaated operating pressure
        self.dateOfChange = dateOfChange
        self.operatingPresure = operatingPressure

    def getDateOfChange(self):
        return(self.dateOfChange)

    def setDateOfChange(self, dateOfChange):
        self.padName = dateOfChange

    def getOperatingPressure(self):
        return(self.operatingPressure)

    def setOperatingPressure(self, operatingPressure):
        self.padName = operatingPressure
