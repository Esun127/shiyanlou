#!/home/shiyanlou/anaconda3/bin/python



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def climate_plot():
    df_temperature = pd.read_excel("GlobalTemperature.xlsx", index_col="Date")
    df_temperature.index = pd.DatetimeIndex(df_temperature.index.values)
    avg_temp = df_temperature.loc[:, ["Land Average Temperature","Land And Ocean Average Temperature"]]

    avg_temp1 = avg_temp.resample('A').mean()
    avg_temp2 = avg_temp.resample('Q').mean()
    
    codelist = ['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE','EN.ATM.NOXE.KT.CE','EN.ATM.GHGO.KT.CE','EN.CLC.GHGR.MT.CE']

    df_climate = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    df_climate = df_climate[df_climate["Series code"].isin(codelist)]  

    df_climate.replace('..', np.nan, inplace=True)
    emission_total = df_climate.iloc[:,6:].T
    emission_total.index = pd.to_datetime(emission_total.index.values, format="%Y", )
    emission_total = emission_total.fillna(method="ffill").fillna(method="bfill").fillna(value=0)    
    emission_total = emission_total.sum(axis=1)
    emission_total = emission_total.resample('A').sum()
    emission_total = emission_total.to_frame(name="Total GHG")



    data = pd.concat((avg_temp1.loc['1990-12-31':'2010-12-31'], emission_total.loc['1990-12-31':'2010-12-31']), axis=1)
    data = data.apply(func=lambda x: (x-x.min())/(x.max()-x.min()))
    data.dropna(axis=0, inplace=True)
    data.index = data.index.year

    fig, axes = plt.subplots(2,2)

    ax = data.plot.line(ax=axes[0,0])
    ax.set_xlabel("Years")
    ax.set_ylabel("Values")

    ax2 = data.plot.bar(ax=axes[0,1])
    ax2.set_xlabel("Years")
    ax2.set_ylabel("Values")


    ax3 = avg_temp2.plot.area(ax=axes[1,0])
    ax3.set_xlabel("Quarters")
    ax3.set_ylabel("Temperature")


    ax4 = avg_temp2.plot.kde(ax=axes[1,1])
    ax4.set_xlabel("Values")
    ax4.set_ylabel("Values")

    plt.show()
    return fig

if __name__ == '__main__':
    print(climate_plot())




