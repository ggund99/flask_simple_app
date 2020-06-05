# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:55:38 2020

@author: ggund
"""


############ Flask app ############



from flask import Flask, request, jsonify
import pickle as pkl
import pandas as pd
import requests
import numpy as np

# load the model


model = pkl.load(open('C:\\Users\\ggund.GARTNER\\Desktop\\hackathon_ltfs\\flask_json_api_python\\regression_model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])


def predict():
    # get data
    data = request.get_json(force = True)
    
    # convert data into dataframe
    data.update((x,[y]) for x,y in data.items())
    
    data_df = pd.DataFrame.from_dict(data)
    
    def transformation(data):
       data['x'] = data['x'].apply(lambda x: np.log(x))
       return(data)
    data_df = transformation(data_df)
    
    data_df = np.array(data_df).reshape(-1,1)
    
    
    result = list(model.predict(data_df))
    
    
    
    # output to screen
    output= {'results': result[0]}
    
    # return output
    return(jsonify(results = output))

if __name__ == '__main__':
    app.run(port = 3030, debug = True, host = '192.168.0.5', use_reloader = True)
    
    
    


    
           

