# -*- coding: utf-8 -*-
from raymond_investment import *

apikey = 'brhMaUKd4jayzZg'

Main.Monitor(category, token)
Main.GetData(ID, token)

CL_seasonality = Commodity.Get_Seasonality('CL', token = apikey)
Strategies = Commodity.Get_SpreadTradingStrategy(token = apikey)
