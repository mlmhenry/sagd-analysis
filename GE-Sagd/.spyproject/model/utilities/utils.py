# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:51:15 2016

@author: 502677886
"""

import functools
import operator


class Utils:

    # def __init__(self):
    # my utility functions

    def sumproduct(*lists):
        return sum(functools.reduce(operator.mul, data) for data in zip(*lists))

    def avg(l):
        return sum(l, 0.0) / len(l)
