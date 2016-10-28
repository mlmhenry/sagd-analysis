# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:25:54 2016

@author: 502677886
"""

# from volume import Volume
# from online import Online
from model.pressure import Pressure
from properties.fluid import Fluid


class Production:

    # constants
    STEAM_CORR = 33.68306
    POWER = 0.24198

    def __init__(self, waterVolume, oilVolume, online, pressure):
#        self.waterVolume = Volume(waterVolume)
#        self.oilVolume = Volume(oilVolume)
#        self.online = Online(online)
#        self.operatingPresure = Pressure(pressure)

        # fluid properties
        self.fluid = Fluid()

        self.waterVolume = waterVolume
        self.oilVolume = oilVolume
        self.producerOnline = online
        self.operatingPressure = pressure

    # water volume produced
    def getWaterVolume(self):
        return(self.waterVolume)

    def setWaterVolume(self, waterVolume):
        self.waterVolume = waterVolume

    # oil volume produced
    def getOilVolume(self):
        return(self.oilVolume)

    def setOilVolume(self, oilVolume):
        self.oilVolume = oilVolume

    # producer hrs online
    def getProducerOnline(self):
        return(self.producerOnline)

    def setProducerOnline(self, online):
        self.producerOnline = online

    # operating pressure
    def getOperatingPressure(self):
        return(self.operatingPressure)

    def setOperatingPressure(self, pressure):
        self.operatingPressure = pressure

    def operatingTemperature(self):
        temperature = self.STEAM_CORR * self.operatingPressure**self.POWER
        return(temperature)

    def oilViscosity(self):
        viscosity = self.fluid.getPropA() * self.operatingPressure**-self.fluid.getPropB()
        return(viscosity)

    def displayProduction(self):
        print(self.waterVolume, ': ', self.oilVolume, ': ', self.producerOnline, ': ', self.operatingPressure)
