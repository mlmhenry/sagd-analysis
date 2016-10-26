# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:01:27 2016

@author: 502677886
"""


class Presure:

    def __init__(self, value):
        self.value = value
        self.unit = 'kPa'

    # operating presure
    def getValue(self):
        return(self.value)

    def setValue(self, value):
        self.value = value

    def getUnit(self):
        return(self.unit)
