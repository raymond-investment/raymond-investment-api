# raymond-investment-api
---
## 使用套件
* pandas
* requests

## 使用方法
現階段為開發階段，所以先以Github這邊公布為主，所以就直接將`raymond_investment.py`給下載至要分析的專案目錄下，之後直接`import raymond_investment`來使用，等待功能更加完整後會在進行pip package的包裝與上傳，未來會持續增加台股、美股等資料功能，以及一些網頁架構的金融分析功能。




## 輸入API Key
初期請查找課前必看章節中有公告原物料課程的API Key，之後可能會提供大家個別註冊帳號並取得各自的API Key



## 抓取資料列表Monitor
在使用資料API之前大家一定很想看看我幫各位準備了哪些資料，這時候就可以利用`Main.Monitor(category,token)`來查找
##### `category`支援的類別如下：
* All
* Equity
* Forex
* FixedIncome
* Commodity

建議可以選定想分析的資產類別後，再針對該大類資產做查找。
```python
from raymond_investment import *
apikey = "xxxxxxxxxxxxxxx" #請見課前必看

df = Main.Monitor(category = 'All', token = apikey)
print(df)
```

## 抓取單一資料
在利用`Monitor`找出自己想要的資訊後，請先記下該資料的`ID`，在使用`Main.GetData(ID,token)`時將`ID`帶入，驗證成功後將會以`pd.DataFrame`回傳，以利後續的時間序列資料運算與分析。
```python
from raymond_investment import *
apikey = "xxxxxxxxxxxxxxx"

data = Main.GetData(ID = 73, token = apikey)
print(data)
```

## 抓取原物料季節性走勢
原物料課程的核心重點就是季節性走勢了，課程中教了兩個計算季節性走勢的做法，一個是利用報酬率來計算，另一種是利用時間序列分析的季節性分解模型，這邊將利用API的方式回傳特定原物料商品的季節性走勢。
```python
from raymond_investment import *
apikey = "xxxxxxxxxxxxxxx" #請見課前必看

data = Commodity.Get_Seasonality('CL', token = apikey)
data.plot()
```
##### 支援商品：
* 西德州原油(CL)
* 布蘭特原油(B)
* 汽油(RB)
* 熱燃油(HO)
* 天然氣(NG)
* 黃豆(S)
* 黃豆油(BO)
* 黃豆粉(SM)
* 小麥(W)
* 玉米(C)
* 白糖(SB)
* 咖啡(KC)
* 可可(CC)
* 棉花(CT)
* 活牛(LC)
* 瘦豬(HE)
* 黃金(GC)
* 白銀(SI)
* 銅(HG)


## 抓取原物料期貨價差交易策略列表
原物料交易最有價值的是利用一多一空的期貨價差，但需要跑的資料非常大量，所以將跑出來的較佳的策略列出，可以供大家直接使用，以下都是根據過去15年的價差資料所產生，抓取方法如下：

```python
from raymond_investment import *
apikey = "xxxxxxxxxxxxxxx" #請見課前必看

strategies = Commodity.Get_SpreadTradingStrategy(token = apikey)
print(strategies)
```








