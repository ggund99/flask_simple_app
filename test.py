# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:56:49 2020

@author: ggund
"""
import json
import requests
import numpy as np
data = {'x':5.23}
data =json.dumps(data)
url = "http://192.168.0.5:3030/"

send_request = requests.post(url, data)
print(send_request)
send_request.json()
