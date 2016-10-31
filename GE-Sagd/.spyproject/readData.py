# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 08:39:10 2016

@author: 502677886
"""

import xlrd
from collections import namedtuple

from model.sagd import Sagd
# from utilities.utils import Utils
from historicalProduction import HistoricalProduction
from inputOil.forecastedOperatingPressure import ForecastedOperatingPressure
from readForecastData import ReadForecastData


class ReadData:

    workbook = xlrd.open_workbook(
       'C:/Users/502677886/Documents/GE GOp/L5P7_SAGDAM_ST_V10.9.6.3.xlsm')
    workbook = xlrd.open_workbook(
       'C:/Users/502677886/Documents/GE GOp/L5P7_SAGDAM_ST_V10.9.6.3.xlsm',
       on_demand = True)
    worksheet = workbook.sheet_by_index(0)
    forecastsheet = workbook.sheet_by_index(5)

    field = []   # The row where we stock the name of the column
    unit = []   # The row where we stock the unit of the column
    data = []
    sagdTable = sagdTable = []
    forcastPressure = []

    # historical production
    productionPressure = []
    productionOilRate = []
    productionOilVolume = []
    productionSteamVolume = []
    productionWaterVolume = []


    def __init__(self, ncols, nrows):
        self.ncols = ncols
        self.nrows = nrows

        # forecast data
        self.fP = []

    def fetchHeader(self):
        for col in range(self.ncols):
            self.field.append(self.worksheet.cell_value(1, col))
            self.unit.append(self.worksheet.cell_value(2, col))

    # transform the workbook to a sagd model (a list of dictionaries)
    def fetchCells(self, nrows, ncols, field, worksheet):
        for row in range(3, nrows):
            elm = {}
#            for col in range(1):
            pad_name = elm[field[0]] = worksheet.cell_value(row, 0)
            pad_date = elm[field[1]] = worksheet.cell_value(row, 1)

            steam_volume = elm[field[3]] = worksheet.cell_value(row, 3)
            injector_online = elm[field[5]] = worksheet.cell_value(row, 5)

            water_volume = elm[field[4]] = worksheet.cell_value(row, 4)
            oil_volume = elm[field[2]] = worksheet.cell_value(row, 2)
            production_online = elm[field[6]] = worksheet.cell_value(row, 6)
            pressure = elm[field[7]] = worksheet.cell_value(row, 7)

            sagd = Sagd(pad_name, pad_date, steam_volume, injector_online,
                        water_volume, oil_volume, production_online,
                        pressure)
            self.sagdTable.append(sagd)

#                elm[field[col]] = worksheet.cell_value(row, col)
#                self.data.append(elm)

    def fetchData(self):
        ReadData.fetchCells(
            self, self.nrows, self.ncols, self.field, self.worksheet)

    def displayData(self, data):
        print(self.data)

    def historicalProduction(self):
        for cell in self.sagdTable:
            if not self.productionOilVolume:
                oilVolume = cell.cummulativeBarrelOilVolume(0)
            else:
                oilVolume = cell.cummulativeBarrelOilVolume(self.productionOilVolume.pop())

            if not self.productionSteamVolume:
                steamVolume = cell.cummulativeBarrelSteamVolume(0)
            else:
                steamVolume = cell.cummulativeBarrelSteamVolume(self.productionSteamVolume.pop())

            if not self.productionWaterVolume:
                waterVolume = cell.cummulativeBarrelWaterVolume(0)
            else:
                waterVolume = cell.cummulativeBarrelWaterVolume(self.productionWaterVolume.pop())

            # current production
            self.productionOilVolume.append(oilVolume)
            self.productionSteamVolume.append(steamVolume)
            self.productionWaterVolume.append(waterVolume)
            self.productionOilRate.append(cell.averageDailyOilRate())
            self.productionPressure.append(cell.production.getOperatingPressure())

#    # transform the workbook to a sagd model
#    def fetchForecastCells(self, nrows, ncols, worksheet):
#        for row in range(27, nrows):
##            dateOfChange = worksheet.cell_value(row, 12)
#            dateFrom = worksheet.cell_value(row, 15)
#            dateTo = worksheet.cell_value(row, 16)
#            pressure = worksheet.cell_value(row, 13)
#            forcastPressure = ForecastedOperatingPressure(dateFrom, dateTo, pressure)
#            self.forcastPressure.append(forcastPressure)

    def fetchForcastData(self, rows):
        ReadData.fetchForecastCells(
            self, rows, self.ncols, self.forecastsheet)

    # forecast pressure (kPa)
    def getForecastPressure(self):
        for cell in self.forcastPressure:
            self.fP.append(cell.getOperatingPressure())
        return(self.fP)

# main program starts here
sheet = ReadData(8, 75)
sheet.fetchHeader()
sheet.fetchData()
model = HistoricalProduction(sheet.sagdTable)
sheet.historicalProduction()
model.historicalProduction()

# sheet.displayData(sheet.data)
sagdSheet = namedtuple('Sagd', 'Well Date OilVolume SteamVolume\
     WaterVolume InjectorOnline ProducerOnline OperatingPressure')
print(sagdSheet._fields)
# cell = sheet.sagdTable.pop()
# print(cell.displaySagd())
print("Sheet sagdTable")
print(sheet.sagdTable[0].production.getOilVolume())

# print(sheet.productionOilVolume, sheet.productionPressure)
print(model.getCurrentOperatingPressure(),
      model.productionMaxOilVolume(), model.productionMaxSteamVolume(),
      model.productionMaxWaterVolume(), model.getProductionRate(),
      model.getAverageOperatingPressure(), model.getAverageProductionUptime(),
      model.mvsReferencePressure())
#for value in iter(sagdSheet._fields):
#    print(value.__getitem__, ', ')

fsheet = ReadForecastData()
fsheet.fetchForcastData(34)
#print(fsheet.getForecastPressure())
#sheet.fetchForcastData(40)
#print(model.getProductionPressure())
#print(sheet.getForecastPressure())
#print(model.getProductionPressure() + sheet.getForecastPressure())
print(fsheet.getForecastPressure())
print(fsheet.getForecastUptime())

model.setFullProfilePressure(fsheet.getFullProfilePressure(model.getProductionPressure()))
print(model.getAverageFullProfilePressure())

model.setFullProfileUptime(fsheet.getFullProfileUptime(model.getProducerUptime()))
print(model.getAverageFullProfileUptime())
print(model.getAverageOperatingTemperature())
