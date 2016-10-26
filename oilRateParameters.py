# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:06:16 2016

@author: 502677886
"""

import math
import operator
import functools

from model.sagd import Sagd
# from model.readData import ReadData
from inputOil.matchOilParameters import MatchOilParameters
from inputOil.inputOilParameters import InputOilParameters


class OilRateParameters:

    # constants
    BUTLER_PEAK_OIL_RATE = 1.30  # FF_P
    ACCELERATIONDUETOGRAVITY = 9.81  # m*s^-2 g
    SECONDS_PER_DAY = 60*60*24  # spd
    PERMEABILITY_DARCIES_TO_M2 = 9.87E-13  # m^2D^-1 Kconv
    BUTLER_EDGE = 2.85E-06
    DECLINE_ORIENTATION = 9.82E5


    def __init__(self):

#        self.matchOilData = MatchOilParameters()
#        self.inputOilData = InputOilParameters()

        # model description
        self.averageOperatingPresure = 3207  # Pop
        self.averageOperatingTemperure = 238  # E6
        self.subCool = 10  # Tsc_P
        self.offset = 2
        # data dhift Mdls
#        self.offset = self.matchOilData.getDataShift()

        # reservoir properties
        self.reservoirTemperture = 12  # Tr_P
        self.grossSteamableHeight = 26.1  # avg height production
#        self.reservoirHeight = 22.1  # self.grossSteamableHeight - averageWedgeThickness
        # avg height production
#        self.grossSteamableHeight = self.inputOilData.getAverageProdHeight()
        # average porosity Ǿ
#        self.averagePorosity = self.inputOilData.getAveragePorosity()
#        self.deltaOilSaturation = self.inputOilData.getDeltaOilSaturation()
#        self.effectivePermeability = self.dynamicPermeability()

        # oil rate parameters
#        self.peakOilRate = 1180  # bbl/d
        self.averageDrainageArea = 100000  # m2
        self.averageHorizontalWellLength = 757  # m
#        self.conformanceFactor = 0.89  # 89%
        self.isorCutoff = 100  # m3/m3
        self.residualAngle = 7
        self.wellPairs = 1
        self.eurVolume = 3.148
        self.obip = 4.72

#        self.sagd = Sagd(name, date, steamVolume, injectorOnline, waterVolume, oilVolume, online, presure)
#        self.model = ReadData(8, 75)

    def sumproduct(*lists):
        return sum(functools.reduce(operator.mul, data) for data in zip(*lists))

    # reservoir height
    def reservoirHeight(self):
        height = self.grossSteamableHeight - self.averageWedgeThickness()
        return(height)

    # effective horizontal wellLength m L
    def effectiveHorizontalWellLength(self):
        length = self.inputOilData.getAverageWellLength() * self.matchOilData.getConformanceFactor()
        return(length)

    # oil rate parameters
    # average unproductive wedge thickness h_up 4.055
    def averageWedgeThickness(self):
        rate = (self.horizontalWellSpacing()/2) * math.tan(self.residualAngle * math.pi/180) * (self.horizontalWellSpacing()/2)/self.horizontalWellSpacing()
        return(rate)

    # horizontal well spacing m Ws 132.1
    def horizontalWellSpacing(self):
        rate = self.averageDrainageArea/self.averageHorizontalWellLength/self.wellPairs
        return(rate)

    # average operating pressure (historical kPa) ###
    def averageOperatingPressure(self):
        # sum(l)/len(l)
        average = sum(self.model.historicalOperatingPresures())/len(self.modelself.model.historicalOperatingPresures())
        return(average)

    # mean viscosity reference pressure ###
    def mvsReferencePressure(self):
        # a(pR/r)**b
        refPressure = self.fluid.getPropA() * (self.sumproduct(self.production.operatingPresure,self.sagd.averageDailyOilRate())/sum(self.sagd.averageDailyOilRate()))**-self.fluid.getPropB()
        return(refPressure)

    # producible recovery factor
    def producibleRecoveryFactor(self):
        factor = (self.eurVolume/self.obip)*100
        return(factor)

    # current production ###
    def currentProduction(self):
        volume = max(self.sagd.cummulativeBarrelOilVolume())
        return(volume)

res = OilRateParameters()
print('reservoir parameters')
print(res.reservoirHeight(), res.SECONDSPERDAY)
print('oil rate parameters')
print(res.averageWedgeThickness(), res.horizontalWellSpacing(), res.producibleRecoveryFactor())
# sagd = Sagd(name, date, steamVolume, injectorOnline, waterVolume, oilVolume, online, presure)
