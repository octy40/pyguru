# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:43:46 2015

@author: muhirwao
"""

# Import modules that will be used
import json
# Use requests to query the API website and assign results to a variable
import requests

#Define function to iterate through the results to get all links

def links():
    z = 0
    for z in range(z,len(results["items"][z])):
        mined_urls.append(results["items"][z]["link"].encode('ascii','ignore'))
        
#iterate through to get 100 images

if __name__ == "__main__":
    # Declare all fixed variables    
    index_num = 1 # index_num represent the number of iterations of the startIndex parameter in order to get 100 images
    mined_urls = []
    key = "AIzaSyDttxqs-uahYWQa2kefZRotb_iAF9jCyW4"
    cx = "008280251192147562951:rghr1k2p058"
    url = "https://www.googleapis.com/customsearch/v1"
    
    #Declare variable to use for input 
    
    input_search = raw_input("Enter 5 search terms separated by commas: ")
    
    input_search_list = input_search.split(',')
    
    i = 0
    
    for i in range(i,len(input_search_list)):
        while index_num != 101:
            parameters = {"q": input_search_list[i],
                      "cx": cx,
                      "key": key,
                      "searchType": "image",
                      "start": index_num,
                      }
            page = requests.request("GET", url, params=parameters)
            results = json.loads(page.text)
            links()
            index_num = index_num + 10
        i = i + 1
        index_num = 1
       
    print 'Number of urls '+str(len(mined_urls))