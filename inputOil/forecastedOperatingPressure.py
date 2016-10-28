# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:34:19 2016

@author: 502677886
"""

import datetime


from model.well import Well
from model.pressure import Pressure


class ForecastedOperatingPressure:

    DEFAULT_PAD = 'L1P1'

    def __init__(self, dateOfChange, operatingPressure):

        # forecaated operating pressure
        self.dateOfChange = Well(self.DEFAULT_PAD, dateOfChange)
        self.operatingPressure = Pressure(operatingPressure)

    # date yyyy-mm-dd
    def getDate(self):
        wellDate = datetime.date.fromordinal(self.dateoffset + int(self.date))
        return(wellDate)

    def getDateOfChange(self):
        return(self.dateOfChange)

    def setDateOfChange(self, dateOfChange):
        self.dateOfChange = dateOfChange

    def getOperatingPressure(self):
        return(self.operatingPressure.getValue())

    def setOperatingPressure(self, operatingPressure):
        self.operatingPressure.setValue(operatingPressure)
