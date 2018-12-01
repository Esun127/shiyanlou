#!/home/shiyanlou/anaconda3/bin/python



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df_temperature = pd.read_excel("GlobalTemperature.xlsx", index_col="Date")
df_temperature.index = pd.DatetimeIndex(df_temperature.index.values)
avg_temp = df_temperature.loc[:, ["Land Average Temperature","Land And Ocean Average Temperature"]]


avg_temp = avg_temp.resample('A').mean()

df_climate = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
df_climate = df_climate[(df_climate["Series code"] == "EN.ATM.CO2E.KT") |\
                             (df_climate["Series code"] == "EN.ATM.METH.KT.CE") |\
                              (df_climate["Series code"] == "EN.ATM.NOXE.KT.CE") |\
                              (df_climate["Series code"] == "EN.ATM.GHGO.KT.CE") |\
                              (df_climate["Series code"] == "EN.CLC.GHGR.MT.CE")]


                              
df_climate.replace('..', np.nan, inplace=True)

emission_total = df_climate.iloc[:,6:].T

emission_total.index = pd.to_datetime(emission_total.index.values, format="%Y", )

emission_total = emission_total.fillna(method="ffill").fillna(method="bfill").fillna(value=0)    
emission_total = emission_total.sum(axis=1)
emission_total = emission_total.resample("A").sum()
emission_total = emission_total.to_frame(name="Total GHG")





data = pd.concat((avg_temp, emission_total), axis=1)
data = data.apply(func=lambda x: (x-x.min())/(x.max()-x.min()))
data.dropna(axis=0, inplace=True)

#print(data)

fig = plt.subplot()

data.plot()
plt.xticks(data.index)
# # fig.plot(x=data.index, y=data.iloc[:,1])

plt.show()
