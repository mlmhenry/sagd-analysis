# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:29:33 2016

@author: 502677886
"""

import datetime


class Well:

    dateoffset = 693594

    def __init__(self, name, date):
        self.pad = name
        self.date = date

    # returns date yyyy-mm-dd
    def getFormatedDate(self):
        wellDate = datetime.date.fromordinal(self.dateoffset + int(self.date))
        return(wellDate)

    # set date from yyyy,mm,dd
    def setDate(self, year, month, day):
        self.date = datetime.date(year, month, day).toordinal()-self.dateoffset

    # pad/well
    def getPad(self):
        return(self.pad)

    def setPad(self, pad):
        self.pad = pad

    # days per month
    def daysPerMonth(self):
        dt = self.getFormatedDate()
        daysPerMonth = (dt.replace(month=dt.month % 12 + 1, day=1) -
                        datetime.timedelta(days=1)).day
        return(daysPerMonth)

    def displayWell(self):
        print(self.pad, ': ', self.getFormatedDate())
