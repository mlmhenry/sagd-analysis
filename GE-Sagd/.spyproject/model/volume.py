# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:49:39 2016

@author: 502677886
"""


class Volume:

    def __init__(self, value):
        self.value = value
        self.unit = 'm3'

    # volume
    def getValue(self):
        return(self.value)

    def setValue(self, value):
        self.value = value

    def getUnit(self):
        return(self.unit)
