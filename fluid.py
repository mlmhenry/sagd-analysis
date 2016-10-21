# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:19:03 2016

@author: 502677886
"""


class Fluid:

    def __init__(self):
        self.a = 0.0226
        self.b = 0.8556

    # fluid properties
    def getPropA(self):
        return(self.a)

    def getPropB(self):
        return(self.b)
