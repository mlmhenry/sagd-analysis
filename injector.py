# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:32:38 2016

@author: 502677886
"""

from volume import Volume
from online import Online


class Injector:

    def __init__(self, volume, online):
        self.steamVolume = Volume(volume)
        self.injectorOnline = Online(online)

#        self.steamVolume = volume
#        self.injectorOnline = online

    # steam volume injected
    def getSteamVolume(self):
        return(self.steamVolume.getValue())

    def setSteamVolume(self, volume):
        self.steamVolume = volume

    def getSteamVolumeUnit(self):
        return(self.steamVolume.getUnit())

    # injector hrs online
    def getInjectorOnline(self):
        return(self.injectorOnline.getValue())

    def setInjectorOnline(self, online):
        self.injectorOnline = online

    def getInjectorOnlineUnit(self):
        return(self.steamVolume.getUnit())

    def displayInjector(self):
        print(self.steamVolume.getValue(), ': ', self.injectorOnline.getValue())
