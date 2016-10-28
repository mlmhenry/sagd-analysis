# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:52:25 2016

@author: 502677886
"""

import xlrd

from constants.const import Const
from model.well import Well
from inputOil.forecastedOperatingPressure import ForecastedOperatingPressure


class ReadForecastData:

    DEFAULT_PAD = 'L1P1'
    CONST = Const()

    workbook = xlrd.open_workbook(
       'C:/Users/502677886/Documents/GE GOp/L5P7_SAGDAM_ST_V10.9.6.3.xlsm')
    workbook = xlrd.open_workbook(
       'C:/Users/502677886/Documents/GE GOp/L5P7_SAGDAM_ST_V10.9.6.3.xlsm',
       on_demand = True)
    forecastsheet = workbook.sheet_by_index(6)

    def __init__(self):

        # default year end well
        self.well = Well(self.CONST.DEFAULT_PAD, 0.0)
        self.well.setDate(2016, 12, 1)

        # forecaste data
        self.forcastPressure = []

    # transform the workbook to a sagd model
    def fetchForecastCells(self, nrows, worksheet):
        for row in range(33, nrows):
            dateOfChange = worksheet.cell_value(row, 12)
            pressure = worksheet.cell_value(row, 13)

            # list forecast data
            forcastPressure = ForecastedOperatingPressure(dateOfChange, pressure)
            self.forcastPressure.append(forcastPressure)

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
        n = 0

        # list full profile pressure
        for cell in self.forcastPressure:
            nrows = self.well.getFormatedDate().month - cell.getDateOfChange().getFormatedDate().month
            if n > 0:
                nrows += 1
            else:
                n += 1
            for row in range(0, nrows):
                self.fP.append(cell.getOperatingPressure())

        return(self.fP)
