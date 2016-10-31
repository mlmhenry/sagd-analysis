# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:41:14 2016

@author: 502677886
"""


class Const:

    DEFAULT_PAD = 'L1P1'

    ACCELERATION_DUE_TO_GRAVITY = 9.81  # m*s^-2 g
    BARRELRATIO = 6.29
    MILLION = 1000000
    PERMEABILITY = 0.99808660947969
    PERMEABILITY_RATIO = 1013249966000
    POWER = 0.24198
    SECONDS_PER_DAY = 60*60*24  # spd
    STEAM_CORR = 33.68306

    def __setattr__(self, *_):
        pass

#    def DEFAULT_PAD():
#        return('L1P1')
#
#    def STEAM_CORR():
#        return '33.68306'
#
#    def POWER():
#        return(0.24198)
