# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 08:39:10 2016

@author: 502677886
"""
from collections import namedtuple
import xlrd

from sagd import Sagd


class ReadData:

    workbook = xlrd.open_workbook(
       'C:/Users/502677886/Documents/GE GOp/L5P7_SAGDAM_ST_V10.9.6.3.xlsm')
    workbook = xlrd.open_workbook(
       'C:/Users/502677886/Documents/GE GOp/L5P7_SAGDAM_ST_V10.9.6.3.xlsm',
       on_demand = True)
    worksheet = workbook.sheet_by_index(0)
    field = []   # The row where we stock the name of the column
    unit = []   # The row where we stock the unit of the column
    data = []
    sagdTable = sagdTable = []

    def __init__(self, ncols, nrows):
        self.ncols = ncols
        self.nrows = nrows

    def fetchHeader(self):
        for col in range(self.ncols):
            self.field.append(self.worksheet.cell_value(1, col))
            self.unit.append(self.worksheet.cell_value(2, col))

    # transform the workbook to a list of dictionaries
    def fetchCells(self, nrows, ncols, field, worksheet):
        for row in range(3, nrows):
            elm = {}
            for col in range(2):
                pad_name = elm[field[0]] = worksheet.cell_value(row, 0)
                pad_date = elm[field[1]] = worksheet.cell_value(row, 1)

                steam_volume = elm[field[3]] = worksheet.cell_value(row, 3)
                injector_online = elm[field[5]] = worksheet.cell_value(row, 5)

                water_volume = elm[field[4]] = worksheet.cell_value(row, 4)
                oil_volume = elm[field[2]] = worksheet.cell_value(row, 2)
                production_online = elm[field[6]] = worksheet.cell_value(row, 6)
                presure = elm[field[7]] = worksheet.cell_value(row, 7)

                sagd = Sagd(pad_name, pad_date, steam_volume, injector_online,
                            water_volume, oil_volume, production_online,
                            presure)
                self.sagdTable.append(sagd)

                elm[field[col]] = worksheet.cell_value(row, col)
                self.data.append(elm)

    def fetchData(self):
        ReadData.fetchCells(
            self, self.nrows, self.ncols, self.field, self.worksheet)

    def displayData(self, data):
        print(self.data)


# main program starts here
sheet = ReadData(8, 75)
sheet.fetchHeader()
sheet.fetchData()
sheet.displayData(sheet.data)
sagdSheet = namedtuple('Sagd', 'Well Date OilVolume SteamVolume\
     WaterVolume InjectorOnline ProducerOnline OperatingPressure')
print(sagdSheet._fields)
cell = sheet.sagdTable.pop()
print(cell.displaySagd())
#for value in iter(sagdSheet._fields):
#    print(value.__getitem__, ', ')
