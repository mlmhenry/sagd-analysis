# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:21:19 2016

@author: 502677886
"""


class MatchOilParameters:

    def __init__(self, dataShift, steamRiseConstant, peakOilRate,
                 declineFactor, conformanceFactor, oilRatCutoff):

        # turning parameters
        # steam chamber height
        self.steamRiseConstant = steamRiseConstant
        # shape factor
        self.declineFactor = declineFactor

        # history match parameters
        self.dataShift = dataShift
        self.peakOilRate = peakOilRate  # bbl/d
        self.conformanceFactor = conformanceFactor  # %
        self.oilRatCutoff = oilRatCutoff  # bbl/day

    def getDataShift(self):
        return(self.dataShift)

    def setDataShift(self, dataShift):
        self.dataShift = dataShift

    def getSteamRiseConstant(self):
        return(self.steamRiseConstant)

    def setSteamRiseConstant(self, steamRiseConstant):
        self.steamRiseConstant = steamRiseConstant

    def getPeakOilRate(self):
        return(self.peakOilRate)

    def setPeakOilRate(self, peakOilRate):
        self.peakOilRate = peakOilRate

    def getDeclineFactor(self):
        return(self.declineFactor)

    def setDeclineFactor(self, declineFactor):
        self.declineFactor = declineFactor

    # a.k.a volumetric sweep efficiency
    def getConformanceFactor(self):
        return(self.conformanceFactor)

    def setConformanceFactor(self, conformanceFactor):
        self.conformanceFactor = conformanceFactor

    def getOilRatCutoff(self):
        return(self.oilRatCutoff)

    def setOilRatCutoff(self, oilRatCutoff):
        self.oilRatCutoff = oilRatCutoff
