# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:57:07 2016

@author: 502677886
"""


class Online:

    def __init__(self, value):
        self.value = value
        self.unit = 'hrs'

    # hrs online
    def getValue(self):
        return(self.value)

    def setValue(self, value):
        self.value = value

    def getUnit(self):
        return(self.unit)
