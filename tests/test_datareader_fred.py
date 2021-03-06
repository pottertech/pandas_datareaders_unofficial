#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run unit tests using
nosetests -s -v
"""

import time
import datetime
from datetime import timedelta

from pandas_datareaders_unofficial import DataReader

import pandas.io.data as web

expire_after = timedelta(hours=1) # 0:no cache - None:no cache expiration

import logging
#import logging.config
#import os

def test_fred():

    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2013, 1, 27)

    #name = "GDP"
    #name = "CPIAUCSL"
    #name = "CPILFESL"
    name = ["CPIAUCSL", "CPILFESL"]
    #name = ["CPIAUCSL", "CPILFESL", "ERROR"]


    data = DataReader("FRED", expire_after=expire_after).get(name, start, end)
    print(data)

    print("="*5 + "Pandas original DataReader" + "="*5)

    gdp = web.DataReader(name, "fred", start, end)

    print(gdp)
    print(type(gdp))
    print(gdp.ix['2013-01-01'])
    print(gdp.dtypes)

    diff = gdp - data
    assert(diff.sum().sum()==0)