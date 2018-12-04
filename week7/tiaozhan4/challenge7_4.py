#!/home/shiyanlou/anaconda3/bin/python


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn import linear_model

def Temperature():
    temp_data = pd.read_csv("GlobalSurfaceTemperature.csv", index_col="Year")
    gas_data = pd.read_csv("GreenhouseGas.csv", index_col="Year")
    
    co2ppm_data = pd.read_csv("CO2ppm.csv", index_col="Year")
    
    data = pd.concat(( gas_data, co2ppm_data, temp_data, ), axis=1)
    
    feature = data.iloc[:,:4].fillna(method="bfill").fillna(method='ffill')

    feature_train = feature.loc["1850":"2010"]
    feature_test = feature.loc["2011":"2017"]

    model = linear_model.LinearRegression()
    ret = []
    for target_column in data.columns.values[-3:]:
        target_train = data[target_column].loc["1850":"2010"]
        model.fit(feature_train, target_train)
        test_predict = model.predict(feature_test)
        ret.append(np.around(test_predict, 3).tolist())
        
    return tuple(ret)

if __name__ == '__main__':
    print(Temperature())
