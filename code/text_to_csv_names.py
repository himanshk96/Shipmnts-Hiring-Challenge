# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:40:53 2018

@author: himansh
"""
import os
names=[]
words=["SHIPPERS NAME & ADDRESS","Shipper's Name and Address","Shipper's Name and Address","s Account Number","Shippers Account Number","SHIPPERS NAME & ADDRESS","Shipper's account Number","Shipper's Name and Address"]
wordsup=["ADD:"]
for i in os.listdir("G:\\shipmnts\\code\\HAWB\\"):
#for i in os.listdir("G:\\shipmnts\\code\\test\\"):
    print (i)
    with open("G:\\shipmnts\\code\\HAWB\\"+i,'r') as f:
        
        text=f.readlines()
    #print ("\n\n\n",text)
    for line in range(len(text)):
        #print (line)
        print(text[line])
        if text[line].strip() in words:
            print(text[line])
                
            if(text[line+1] == "" or text[line+1][0].isdigit() or text[line+1].strip() == "Shipper's Account Number"):
                        
                
                if(text[line+2].strip() == "Shipper's Account Number"):
                    names.append([i,text[line+3]])
                    break
                else:
                    names.append([i,text[line+2]])
                    break
            else: names.append([i,text[line+1]]); break
print (names)
import pandas as pd
files=[name[0] for name in names]
name_=[name[1].strip() for name in names]

df=pd.DataFrame(list(zip(files,name_)))

df.to_csv('HAWB_shippers.csv',header=False)