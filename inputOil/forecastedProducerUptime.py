# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:43:17 2016

@author: 502677886
"""


class ForecastedProducerUptime:

    def __init__(self, dateOfChange, uptime):

        # forecaated producer uptime
        self.dateOfChange = dateOfChange
        self.operatingPresure = uptime

    def getDateOfChange(self):
        return(self.dateOfChange)

    def setDateOfChange(self, dateOfChange):
        self.padName = dateOfChange

    def getOperatingPressure(self):
        return(self.uptime)

    def setOperatingPressure(self, uptime):
        self.padName = uptime
