# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:35:27 2016

@author: 502677886
"""

from utilities.utils import Utils


class HistoricalProduction:

    # historical production
    productionPresure = []
    productionOilRate = []
    productionOilVolume = []
    productionSteamVolume = []
    productionWaterVolume = []
    productionRate = 0.0
    averageOperatingPresure = 0.0
    currentOperatingPresure = 0.0

    def __init__(self, sagdTable):
        self.sagdTable = sagdTable

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
            self.productionPresure.append(cell.production.getOperatingPresure())
            self.productionRate = max(self.productionSteamVolume)/max(self.productionOilVolume)
            self.currentOperatingPresure = Utils.sumproduct(self.productionPresure, self.productionOilRate)/sum(self.productionOilRate)
            self.averageOperatingPresure = Utils.avg(self.productionPresure)

    def getCurrentOperatingPresure(self):
        return(self.currentOperatingPresure)

    def maxProductionOilVolume(self):
        return(max(self.productionOilVolume))