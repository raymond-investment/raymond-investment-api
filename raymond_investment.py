# -*- coding: utf-8 -*-

import pandas as pd
import requests

class Main:
    @staticmethod
    def Monitor(category, token):
        if category == 'All':
            df = pd.read_json(f"https://app.raymond-investment.com/data/api/monitor?token={token}").transpose().sort_index()
        
        elif category == 'Equity':
            df = pd.read_json(f"https://app.raymond-investment.com/data/api/monitor/Equity?token={token}").transpose().sort_index()
            
        elif category == 'Forex':
            df = pd.read_json(f"https://app.raymond-investment.com/data/api/monitor/Forex?token={token}").transpose().sort_index()
            
        elif category == 'FixedIncome':
            df = pd.read_json(f"https://app.raymond-investment.com/data/api/monitor/FixedIncome?token={token}").transpose().sort_index()
        
        elif category == 'Commodity':
            df = pd.read_json(f"https://app.raymond-investment.com/data/api/monitor/Commodity?token={token}").transpose().sort_index()
        
        else:
            print("Wrong input.")
        
        return df[['ID','Name_Chinese','Name_English','Category','Frequency','StartDate','EndDate','NumberOfData']]



    #抓取資料
    @staticmethod
    def GetData(ID, token, Start=None, End=None):
        if (Start == None) & (End == None):
            url = f"https://app.raymond-investment.com/data/api?ID={ID}&token={token}"
        elif (Start != None) & (End == None):
            url = f"https://app.raymond-investment.com/data/api?ID={ID}&StartDate={Start}&token={token}"
        elif (Start == None) & (End != None):
            url = f"https://app.raymond-investment.com/data/api?ID={ID}&EndDate={End}&token={token}"
        else:
            url = f"https://app.raymond-investment.com/data/api?ID={ID}&StartDate={Start}&EndDate={End}&token={token}"
        
        res = requests.get(url)
        
        df = pd.DataFrame.from_dict(res.json()['data']).transpose()
        df.index = df['Date']
        df.index = pd.to_datetime(df.index)
        
        
        return df[['Value']].sort_index()



class Commodity:
    #抓取原物料價差交易
    @staticmethod
    def Get_SpreadTradingStrategy(token):
        url = "https://app.raymond-investment.com/api/commodities/spread_strategy"
        payload = {'token':token}
        res = requests.get(url, params = payload)
        
        df = pd.DataFrame.from_dict(res.json()).transpose().sort_values('EntryDate')
        
        return df.reset_index()
        
        
    #抓取原物料季節性走勢
    @staticmethod
    def Get_Seasonality(symbol,token):
        url = f"https://app.raymond-investment.com/api/commodities/seasonality/{symbol}"
        payload = {'token':token}
        res = requests.get(url, params = payload)
        
        df = pd.DataFrame.from_dict(res.json()).transpose()
        df.columns = [symbol + ' Seasonality']
        return df

















