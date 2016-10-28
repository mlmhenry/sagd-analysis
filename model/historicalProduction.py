# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:35:27 2016

@author: 502677886
"""

from utilities.utils import Utils
from properties.fluid import Fluid
from inputOil.forecastedOperatingPressure import ForecastedOperatingPressure

class HistoricalProduction:

    def __init__(self, sagdTable):

        # historical production data
        self.sagdTable = sagdTable

        # historical production
        self.productionPressure = []
        self.productionOilRate = []
        self.productionOilVolume = []
        self.productionSteamVolume = []
        self.productionWaterVolume = []
        self.productionUptime = []

        # fluid properties
        self.fluid = Fluid()


    def historicalProduction(self):
        for cell in self.sagdTable:

            # cummulative oil volume mmbbl
            if not self.productionOilVolume:
                oilVolume = cell.cummulativeBarrelOilVolume(0)
            else:
                oilVolume = cell.cummulativeBarrelOilVolume(self.productionOilVolume.pop())

            # cummulative steam volume mmbbl
            if not self.productionSteamVolume:
                steamVolume = cell.cummulativeBarrelSteamVolume(0)
            else:
                steamVolume = cell.cummulativeBarrelSteamVolume(self.productionSteamVolume.pop())

            # cummulative water volume mmbbl
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
            self.productionUptime.append(cell.producerUptime())


    def forcast(self, dateOfChange, operatingPressure):

        self.forcastPressure = ForecastedOperatingPressure(dateOfChange, operatingPressure)
        self.forcastPressure.getOperatingPressure()
#        cell.production.setOperatingPressure(self.forcastPressure.)

    # current production oil volume mmbbl
    def productionMaxOilVolume(self):
        return(max(self.productionOilVolume))

    # current production steam volume mmbbl
    def productionMaxSteamVolume(self):
        return(max(self.productionSteamVolume))

    # current production water volume mmbbl
    def productionMaxWaterVolume(self):
        return(max(self.productionWaterVolume))

    # current production cSOR
    def getProductionRate(self):
        return(max(self.productionSteamVolume)/max(self.productionOilVolume))

    # current production operating pressure
    def getCurrentOperatingPressure(self):
        return(Utils.sumproduct(self.productionPressure, self.productionOilRate)/sum(self.productionOilRate))

    # average operating pressure (historical kPa)
    def getAverageOperatingPressure(self):
        return(Utils.avg(self.productionPressure))

    # well up-time (historical)
    def getAverageProductionUptime(self):
        return(Utils.avg(self.productionUptime))

    # mean viscosity at reference pressure
    def mvsReferencePressure(self):
        # a(pR/r)**b
        refPressure = self.fluid.getPropA() * self.getCurrentOperatingPressure()**(-self.fluid.getPropB())
        return(refPressure)

    # production pressure (historical kPa)
    def getProductionPressure(self):
        return(self.productionPressure)

    # average operating pressure (full profile kPa)
    def getAverageFullProfilePressure(self, fullProfilePressure):
        return(Utils.avg(fullProfilePressure))

