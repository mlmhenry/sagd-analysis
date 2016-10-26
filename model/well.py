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

    # date yyyy-mm-dd
    def getDate(self):
        wellDate = datetime.date.fromordinal(self.dateoffset + int(self.date))
        return(wellDate)

    # pad/well
    def getPad(self):
        return(self.pad)

    # days per month
    def daysPerMonth(self):
        dt = self.getDate()
        daysPerMonth = (dt.replace(month=dt.month % 12 + 1, day=1) -
                        datetime.timedelta(days=1)).day
        return(daysPerMonth)

    def displayWell(self):
        print(self.pad, ': ', self.getDate())
