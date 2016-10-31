# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:06:16 2016

@author: 502677886
"""

import math
#import operator
#import functools

from model.constants.const import Const
from model.sagd import Sagd
#from model.readData import ReadData
from inputOil.matchOilParameters import MatchOilParameters
from inputOil.inputOilParameters import InputOilParameters


class OilRateParameters:

    # constants
    CONST = Const()
    BUTLER_PEAK_OIL_RATE = 1.30  # FF_P
    ACCELERATION_DUE_TO_GRAVITY = 9.81  # m*s^-2 g
    SECONDS_PER_DAY = 60*60*24  # spd
    PERMEABILITY_DARCIES_TO_M2 = 9.87E-13  # m^2D^-1 Kconv
    BUTLER_EDGE = 2.85E-06
    DECLINE_ORIENTATION = 9.82E5


    def __init__(self, pad, wp, averageHeight, averagePorosity,
                 averageOilSaturation, averageDrainageArea, averageWellLength,
                 residualOilSaturation, residualAngle):

#        self.matchOilData = MatchOilParameters()
        self.inputOilData = InputOilParameters(pad, wp, averageHeight, averagePorosity,
                 averageOilSaturation, averageDrainageArea, averageWellLength,
                 residualOilSaturation, residualAngle)

        # model description
        self.averageOperatingPressure = 3207  # Pop
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
        self.grossSteamableHeight = self.inputOilData.getAverageProdHeight()
        # average porosity Ǿ
        self.averagePorosity = self.inputOilData.getAveragePorosity()
        self.initialOilSaturation = self.inputOilData.getAverageOilSaturation()
#        self.deltaOilSaturation = self.inputOilData.getDeltaOilSaturation()
#        self.effectivePermeability = self.dynamicPermeability()

        # oil rate parameters
#        self.peakOilRate = 1180  # bbl/d
        self.peakOilRate = self.matchOilData.getPeakOilRate()
        self.averageDrainageArea = 100000  # m2
#        self.averageHorizontalWellLength = 757  # m
        self.averageHorizontalWellLength = self.inputOilData.getAverageWellLength()
#        self.conformanceFactor = 0.89  # 89%
        self.isorCutoff = 100  # m3/m3
        self.residualAngle = 7
        self.wellPairs = 1
        self.eurVolume = 3.148 ###
        self.obip = 4.72 ###

        # thermal diffusivity - reservoir
        self.thermalDiffusivityReservoir = 5.4798E-07

#        self.sagd = Sagd(name, date, steamVolume, injectorOnline, waterVolume, oilVolume, online, pressure)
#        self.model = ReadData(8, 75)

#    def sumproduct(*lists):
#        return sum(functools.reduce(operator.mul, data) for data in zip(*lists))

    # height of reservoir top above producer (E12-h_UP 22.1)
    def reservoirHeight(self):
        height = self.grossSteamableHeight - self.averageWedgeThickness()
        return(height)

    # effective horizontal wellLength m L
    def effectiveHorizontalWellLength(self):
        length = self.inputOilData.getAverageWellLength() * self.matchOilData.getConformanceFactor()
        return(length)

    # oil rate parameters
    # average unproductive wedge thickness (h_up 4.055)
    def averageWedgeThickness(self):
        rate = (self.horizontalWellSpacing()/2) * math.tan(self.residualAngle * math.pi/180) * (self.horizontalWellSpacing()/2)/self.horizontalWellSpacing()
        return(rate)

    # horizontal well spacing m Ws 132.1
    def horizontalWellSpacing(self):
        rate = self.averageDrainageArea/self.averageHorizontalWellLength/self.wellPairs
        return(rate)

    # producible recovery factor ###
    def producibleRecoveryFactor(self):
        factor = (self.eurVolume/self.obip)*100
        return(factor)

    # original bitumen in place (OBIP mmbbl) ###
    def originalBitumenPlace(self):
        factor = self.horizontalWellSpacing() * self.averageHorizontalWellLength * self.grossSteamableHeight * self.initialOilSaturation * self.averagePorosity * self.CONST.BARRELRATIO/self.CONST.MILLION
        return(factor)

    # effective or dynamic permeability (D Keff Darcys) ###
    def effectivePermeability(self):
        factor = ((self.peakOilRate/self.CONST.BARRELRATIO/self.CONST.PERMEABILITY/(self.CONST.SECONDS_PER_DAY))**2*self.model.mvsReferencePressure())/(4*(self.averageHorizontalWellLength^2)*1.3*self.CONST.ACCELERATION_DUE_TO_GRAVITY*self.averagePorosity*self.thermalDiffusivityReservoir*self.inputOilData.deltaOilSaturation*self.reservoirHeight())*self.CONST.PERMEABILITY_RATIO
        return(factor)

    # average operating pressure (historical kPa) ###
#    self.model.getAverageOperatingPressure()

    # current production oil volume mmbbl ###
#    self.model.productionMaxOilVolume()

    # mean viscosity at reference pressure ###
#    self.model.mvsReferencePressure()



#res = OilRateParameters(pad, wp, averageHeight, averagePorosity,
#                 averageOilSaturation, averageDrainageArea, averageWellLength,
#                 residualOilSaturation, residualAngle)
res = OilRateParameters('LP1P5', 1, 26.14, 0.32, 0.89, 100000, 757, 0.10, 7)
print('reservoir parameters')
print(res.reservoirHeight(), res.SECONDS_PER_DAY)
print('oil rate parameters')
print(res.averageWedgeThickness(), res.horizontalWellSpacing(), res.producibleRecoveryFactor())
print(res.horizontalWellSpacing(), res.averageHorizontalWellLength, res.grossSteamableHeight, res.initialOilSaturation, res.averagePorosity, res.CONST.BARRELRATIO, res.CONST.MILLION)
print(res.originalBitumenPlace())
print(res.effectivePermeability())
# sagd = Sagd(name, date, steamVolume, injectorOnline, waterVolume, oilVolume, online, pressure)
