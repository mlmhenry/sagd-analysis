# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:52:25 2016

@author: 502677886
"""

import xlrd

from model.constants.const import Const
from model.well import Well
from inputOil.forecastedOperatingPressure import ForecastedOperatingPressure
from inputOil.forecastedProducerUptime import ForecastedProducerUptime


class ReadForecastData:

    CONST = Const()

    workbook = xlrd.open_workbook(
       'C:/Users/502677886/Documents/GE GOp/L5P7_SAGDAM_ST_V10.9.6.3.xlsm')
    workbook = xlrd.open_workbook(
       'C:/Users/502677886/Documents/GE GOp/L5P7_SAGDAM_ST_V10.9.6.3.xlsm',
       on_demand = True)
    forecastsheet = workbook.sheet_by_index(5)

    def __init__(self):

        # default year end well
        self.well = Well(self.CONST.DEFAULT_PAD, 0.0)
        self.well.setDate(2016, 12, 1)

        # forecaste data
        self.forcastPressure = []
        self.forcastUptime = []

    # transform the worksheet to a sagd model
    def fetchForecastCells(self, nrows, worksheet):
        for row in range(27, nrows):
#            dateOfChange = worksheet.cell_value(row, 12)
            dateFrom = worksheet.cell_value(row, 14)
            dateTo = worksheet.cell_value(row, 15)
            pressure = worksheet.cell_value(row, 16)

            dateFromUptime = worksheet.cell_value(row, 18)
            dateToUptime = worksheet.cell_value(row, 19)
            uptime = worksheet.cell_value(row, 20)

            # list forecast data
            forcastPressure = ForecastedOperatingPressure(dateFrom, dateTo, pressure)
            self.forcastPressure.append(forcastPressure)

            forcastUptime = ForecastedProducerUptime(dateFromUptime, dateToUptime, uptime)
            self.forcastUptime.append(forcastUptime)

    def fetchForcastData(self, rows):
        ReadForecastData.fetchForecastCells(
            self, rows, self.forecastsheet)

    # forecast pressure (kPa)
    def getForecastPressure(self):
        self.fP = []

        # list forecast pressure
        for cell in self.forcastPressure:
            self.fP.append(cell.getOperatingPressure())
        return(self.fP)

    # full profile pressure (kPa)
    def getFullProfilePressure(self, historicalPressure):
        self.fP = historicalPressure

        # list full profile pressure
        for cell in self.forcastPressure:
#            nrows = self.well.getFormatedDate().month - cell.getDateOfChange().getFormatedDate().month
            nrows = (cell.getDateTo().getFormatedDate() - cell.getDateFrom().getFormatedDate()).days

            # number of days to number on months
            if nrows > 365:
                nrows = int(nrows/365*12) + 1
            else:
                nrows = int(nrows/28) - 1

            # one row per month
            for row in range(0, nrows):
                self.fP.append(cell.getOperatingPressure())

        return(self.fP)

    # forecast producer uptime (%/100)
    def getForecastUptime(self):
        self.fP = []

        # list forecast uptime
        for cell in self.forcastUptime:
            self.fP.append(cell.getProducerUptime())
        return(self.fP)

    # full profile uptime (%/100)
    def getFullProfileUptime(self, historicalUptime):
        self.ft = historicalUptime

        # list full profile uptime
        for cell in self.forcastUptime:
#            nrows = self.well.getFormatedDate().month - cell.getDateOfChange().getFormatedDate().month
            nrows = (cell.getDateTo().getFormatedDate() - cell.getDateFrom().getFormatedDate()).days

            # number of days to number on months
            if nrows > 365:
                nrows = int(nrows/365*12) + 1
            else:
                nrows = int(nrows/28) - 1

            # one row per month
            for row in range(0, nrows):
                self.ft.append(cell.getProducerUptime())

        return(self.ft)

