# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:34:12 2020

@author: ggund
"""

path = "C:\\Users\\ggund.GARTNER\\Desktop\\hackathon_ltfs\\flask_json_api_python"
import os
os.chdir(path)
import json
import pickle as pkl
from flask import Flask
import pandas as pd
from flask import Flask
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import random
import numpy as np
from sklearn.metrics import mean_absolute_error
n = 100
x = [float(random.randrange(1,100)) for i in range(n)  ]
y= [float(np.random.rand(1)) for i in range(n) ]

df = pd.DataFrame({"x":x, "y":y}) 
df1 = df.to_json()

# transformation

def transformation(data):
    data['x'] = data['x'].apply(lambda x: np.log(x))
    return(data)

train, test = train_test_split(df, test_size = 0.2) 

train =  transformation(data = train)

test = transformation(data = test)


x_train = np.array(train['x']).reshape(-1,1)
y_train = train['y']
x_test  = np.array(test['x']).reshape(-1,1)
y_test = test['y']

model = LinearRegression()

model.fit(x_train, y_train)

predict1  = model.predict(x_test.reshape(-1,1))

mae = mean_absolute_error(y_test, predict1)

# save model
pkl.dump(model, open("regression_model.pkl", 'wb'))


