# -*- coding: utf-8 -*-
from raymond_investment import *

apikey = 'XXXXXXXXXXXXXXXXX'

Monitor = Main.Monitor(category = 'All', token = apikey)
print(Monitor)
#Main.GetData(ID, token)

#CL_seasonality = Commodity.Get_Seasonality('CL', token = apikey)
#Strategies = Commodity.Get_SpreadTradingStrategy(token = apikey)

