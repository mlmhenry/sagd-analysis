# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:36:39 2016

@author: 502677886
"""

from well import Well
from injector import Injector
from production import Production


class Sagd:

    HOURSPERDAY = 24
    BARRELRATIO = 6.29
    MILLIONS = 1000000

    def __init__(self, name, date, steamVolume, injectorOnline, waterVolume, oilVolume, online, presure):
        self.well = Well(name, date)
        self.production = Production(waterVolume, oilVolume, online, presure)
        self.injector = Injector(steamVolume, injectorOnline)

    # average daily oil rate
    def averageDailyOilRate(self):
        rate = self.production.getOilVolume()/self.well.daysPerMonth()
        return(rate)

    # barrel daily oil rate
    def barrelOilRate(self):
        rate = (self.production.getOilVolume()/self.well.daysPerMonth()) * self.BARRELRATIO
        return(rate)

    # barrel oil per millions
    def barrelOilRatePM(self):
        rate = self.production.getOilVolume() * self.BARRELRATIO/self.MILLIONS
        return(rate)

    # cummulative oil volume produced
    def cummulativeOilVolume(self, cummulativeOilVolume):
        cum = self.averageDailyOilRate() * self.well.daysPerMonth()
        if cummulativeOilVolume == 0:
            cummulativeOilVolume = cum
        else:
            cummulativeOilVolume += cum
        return(cummulativeOilVolume)

    # average daily oil steam injected
    def averageDailySteam(self):
        rate = self.injector.getSteamVolume()/self.well.daysPerMonth()
        return(rate)

    # barrel daily steam rate
    def barrelSteamRate(self):
        rate = (self.injector.getSteamVolume()/self.well.daysPerMonth()) * self.BARRELRATIO
        return(rate)

    # barrel steam per millions
    def barrelSteamRatePM(self):
        rate = self.injector.getSteamVolume() * self.BARRELRATIO/self.MILLIONS
        return(rate)

    # cummulative steam produced
    def cummulativeSteamVolume(self, cummulativeSteamVolume):
        cum = self.averageDailySteam() * self.well.daysPerMonth()
        if cummulativeSteamVolume == 0:
            cummulativeSteamVolume = cum
        else:
            cummulativeSteamVolume += cum
        return(cummulativeSteamVolume)

    # average daily oil water produced
    def averageDailyWater(self):
        rate = self.production.getWaterVolume()/self.well.daysPerMonth()
        return(rate)

    # barrel water per millions
    def barrelWaterRatePM(self):
        rate = self.production.getWaterVolume() * self.BARRELRATIO/self.MILLIONS
        return(rate)

    # cummulative water produced
    def cummulativeWaterVolume(self, cummulativeWaterVolume):
        cum = self.averageDailyWater() * self.well.daysPerMonth()
        if cummulativeWaterVolume == 0:
            cummulativeWaterVolume = cum
        else:
            cummulativeWaterVolume += cum
        return(cummulativeWaterVolume)

    # water steam ratio
    def waterSteamRatio(self):
        rate = self.averageDailyWater()/self.averageDailySteam()
        return(rate)

    # instantaneous steam oil ratio
    def steamOilRatio(self):
        rate = self.averageDailySteam()/self.averageDailyOilRate()
        return(rate)

    # cummulative steam oil ratio
    def cummulativeSteamOilRatio(self, cummulativeSteamVolume, cummulativeOilVolume):
        rate = self.cummulativeSteamVolume(cummulativeSteamVolume)/self.cummulativeOilVolume(cummulativeOilVolume)
        return(rate)

    # instantaneous water steam ratio
    def waterSteamRatio(self):
        rate = self.averageDailyWater()/self.averageDailySteam()
        return(rate)

    # cummulative water steam ratio
    def cummulativeWaterSteamRatio(self):
        rate = self.barrelWaterRatePM()/self.barrelSteamRatePM()
        return(rate)

    # injector uptime percent
    def injectorUptime(self):
        percent = self.injector.getInjectorOnline()/(self.well.daysPerMonth() * self.HOURSPERDAY)

        # if longer than a day
        if self.injector.getInjectorOnline() >= (self.well.daysPerMonth() * self.HOURSPERDAY):
            percent = 1
        return(percent)

    # producer uptime percent
    def producerUptime(self):
        percent = self.production.getProducerOnline()/(self.well.daysPerMonth() * self.HOURSPERDAY)

        # if longer than a day
        if self.production.getProducerOnline() >= (self.well.daysPerMonth() * self.HOURSPERDAY):
            percent = 1
        return(percent)

    def displaySagd(self):
        print(self.well.displayWell())
        print(self.injector.displayInjector())
        print(self.production.displayProduction())


sagd = Sagd('L1P5', 40513, 6205.05, 720, 5166.2656, 346.46, 720,
            3211.92525227865)
sagd2 = Sagd('L1P5', 40483, 5055.453199999999, 602.9905, 5034.1051, 255.65019999999998, 744.0,
            2886.3965652988804)
print(sagd.displaySagd())
print(sagd.well.daysPerMonth(), ': ', sagd.production.getOilVolume(),
      ': ', sagd.averageDailyOilRate(), sagd.cummulativeOilVolume(0),
      sagd.averageDailySteam(), sagd.cummulativeSteamVolume(0),
      sagd.averageDailyWater(), sagd.cummulativeWaterVolume(0),
      sagd.waterSteamRatio(), sagd.steamOilRatio(), sagd.cummulativeSteamOilRatio(0, 0),
      sagd.injectorUptime(), sagd.producerUptime(), sagd.production.operatingTemperature(),
      sagd.barrelOilRate(), sagd.barrelOilRatePM(),
      sagd.barrelSteamRate(), sagd.barrelSteamRatePM(),
      sagd.barrelWaterRatePM(), sagd.waterSteamRatio(), sagd.cummulativeWaterSteamRatio(),
      sagd.production.oilViscosity())

print(sagd2.displaySagd())
print(sagd2.well.daysPerMonth(), ': ', sagd2.production.getOilVolume(),
      ': ', sagd2.averageDailyOilRate(), sagd2.cummulativeOilVolume(165),
      sagd2.cummulativeSteamVolume(5143), sagd2.cummulativeWaterVolume(3956),
      sagd2.steamOilRatio(), sagd2.cummulativeSteamOilRatio(5143, 165),
      sagd2.injectorUptime(), sagd2.producerUptime(), sagd2.production.operatingTemperature(),
      sagd2.barrelOilRate(), sagd.barrelOilRatePM())
