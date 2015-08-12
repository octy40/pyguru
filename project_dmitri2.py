# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:43:46 2015

@author: muhirwao
"""

# Import modules that will be used

import json
import requests

# Declare fixed variables

mined_urls = []
key = "AIzaSyDttxqs-uahYWQa2kefZRotb_iAF9jCyW4"
cx = "008280251192147562951:rghr1k2p058"
url = "https://www.googleapis.com/customsearch/v1"
parameters = {"q": "banana",
              "cx": cx,
              "key": key,
              "searchType": "image",
              "start": results["queries"]["nextPage"][0]["startIndex"],
              }

# Use requests to query the API website and assign results to a variable
page = requests.request("GET", url, params=parameters)
results = json.loads(page.text)


#iterate through the results to get all links

def links():
    for z in range(z,len(results["items"][0])):
        


print results["searchInformation"]
