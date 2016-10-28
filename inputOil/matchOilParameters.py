# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:21:19 2016

@author: 502677886
"""


class MatchOilParameters:

    def __init__(self, dataShift, steamRiseConstant, peakOilRate,
                 declineFactor, conformanceFactor, oilRateCutoff):

        # turning parameters
        # steam chamber height
        self.steamRiseConstant = steamRiseConstant
        # shape factor
        self.declineFactor = declineFactor

        # history match parameters
        self.dataShift = dataShift
        self.peakOilRate = peakOilRate  # bbl/d
        self.conformanceFactor = conformanceFactor  # %
        self.oilRateCutoff = oilRateCutoff  # bbl/day

    # data shift
    def getDataShift(self):
        return(self.dataShift)

    def setDataShift(self, dataShift):
        self.dataShift = dataShift

    # steam rise constant (aka steam chamber height)
    def getSteamRiseConstant(self):
        return(self.steamRiseConstant)

    def setSteamRiseConstant(self, steamRiseConstant):
        self.steamRiseConstant = steamRiseConstant

    # peak oil rate
    def getPeakOilRate(self):
        return(self.peakOilRate)

    def setPeakOilRate(self, peakOilRate):
        self.peakOilRate = peakOilRate

    # decline factor (aka shape factor)
    def getDeclineFactor(self):
        return(self.declineFactor)

    def setDeclineFactor(self, declineFactor):
        self.declineFactor = declineFactor

    # conformance factor a.k.a volumetric sweep efficiency
    def getConformanceFactor(self):
        return(self.conformanceFactor)

    def setConformanceFactor(self, conformanceFactor):
        self.conformanceFactor = conformanceFactor

    # oil rate cutoff
    def getOilRatCutoff(self):
        return(self.oilRateCutoff)

    def setOilRateCutoff(self, oilRateCutoff):
        self.oilRateCutoff = oilRateCutoff
