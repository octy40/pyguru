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
    
    print "\nYou're going to enter multiple search terms, but we'll use only one for now\n"
    
    search_term1 = raw_input("Enter first search term: ")
    search_term2 = raw_input("Enter second search term: ")
    search_term3 = raw_input("Enter third search term: ")
    search_term4 = raw_input("Enter forth search term: ")
    
    while index_num != 101:
        parameters = {"q": search_term1,
                  "cx": cx,
                  "key": key,
                  "searchType": "image",
                  "start": index_num,
                  }
        page = requests.request("GET", url, params=parameters)
        results = json.loads(page.text)
        links()
        index_num = index_num + 10
    
    print 'Number of urls '+str(len(mined_urls))
        
