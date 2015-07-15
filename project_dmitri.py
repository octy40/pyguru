# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:20:59 2015

@author: muhirwao
"""

from os import listdir
from os.path import isfile, join

mypath = "C:\users\muhirwao\Desktop\Archive\instruments"

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

#Remove .jpg from each string. Since the first element in the list is '.DS_Store' we'll start iterating from 1

k = 1
onlyfiles_good = []
for k in range(k,len(onlyfiles)):
    if ('.jpg' in onlyfiles[k]):
        onlyfiles_good.append(onlyfiles[k].replace('.jpg',''))
    elif ('.JPG' in onlyfiles[k]):
        onlyfiles_good.append(onlyfiles[k].replace('.JPG',''))
    else:
        onlyfiles_good.append(onlyfiles[k])
        
import pandas as pd

#Read Excel file using Pandas. Pandas turns it into a data frame

newFile = pd.read_excel("C:\Users\muhirwao\Desktop\Archive\instdesc.xlsx")

#Convert the data frame into a list

newFile_tolist = newFile.values.tolist() #this returns a list thatt's in another list

# Create another list and store the first column of the excel sheet i.e the list with index [0]

i = 0
data = []
for i in range(i,len(newFile_tolist)):
    data.append(newFile_tolist[i][0])
    
#Remove u' from each element in the list

z = 0
data_good = []
for z in range(z,len(data)):
    if type(data[z]) == unicode:
        data_good.append(data[z].encode('ascii','ignore'))
    else:
        data_good.append(data[z])
print data_good
