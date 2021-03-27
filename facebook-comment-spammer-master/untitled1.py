# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:08:30 2020

@author: user
"""

import http.client, urllib 
from bs4 import BeautifulSoup 
import os 
import json
import time

access_token='EAAFYfkmP4UcBADsGPuqy1qAiDXV6Wdz7M7ZC3VgaP73Q1XeWx34aMUZAtAoYfT09aIEqnMojIgfe1q8BbcZC65prqeRXZCJIxRuVvtG4ZByvVTX9bN236yj1MqO5LFSRVXMjULrFEVwFDdlE9SJ1DZAPMGThGJ4DYtWnJxReHeD1LIZAFkJD0Tj9pZADmrItu7c92JHIKDji8Thi6dgzYQmO'
# access_token = raw_input('Paste your access token here :')

conn = http.client.HTTPSConnection("graph.facebook.com") 
print('Please Wait!')
 
def comment(url): 
    connect = http.client.HTTPSConnection("graph.facebook.com") 
    connect.request("GET",url) 
    for x in range(10): # make it 10, 100, 1000, 10000  
            
            print('commenting %d '% x)
            #path ='/'+'100157971923605'+'/comments'
            path ='https://www.facebook.com/saba.maleki.756/posts/110837557510557'
            param_data={  'format':'json', 
                        'message':'<3', # change message from here
                        'access_token':access_token 
                  } 
            connect = http.client.HTTPSConnection("graph.facebook.com") 
            connect.request("POST",path,urllib.parse.urlencode(param_data),{}) 
            print('h')
            time.sleep(0.09)
           
url='https://www.facebook.com/saba.maleki.756' 
comment(url) 
print('DONE!')

# "id": "100156118590457_100157971923605"
