# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:34:19 2016

@author: 502677886
"""


from model.constants.const import Const
from model.well import Well
from model.pressure import Pressure


class ForecastedProducerUptime:

    CONST = Const()

    def __init__(self, dateFrom, dateTo, uptime):

        # forecaated operating pressure
#        self.dateOfChange = Well(self.CONST.DEFAULT_PAD, dateOfChange)
        self.dateFrom = Well(self.CONST.DEFAULT_PAD, dateFrom)
        self.dateTo = Well(self.CONST.DEFAULT_PAD, dateTo)
        self.uptime = Pressure(uptime)

    def getDateTo(self):
        return(self.dateTo)

    def setDateTo(self, dateTo):
        self.dateTo = dateTo

    def getDateFrom(self):
        return(self.dateFrom)

    def setDateFrom(self, dateFrom):
        self.dateFrom = dateFrom

    def getDateOfChange(self):
        return(self.dateOfChange)

    def setDateOfChange(self, dateOfChange):
        self.dateOfChange = dateOfChange

    def getProducerUptime(self):
        return(self.uptime.getValue())

    def setProducerUptime(self, uptime):
        self.uptime.setValue(uptime)
