# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### data read
import pandas as pd
#import numpy as np
import json

#### OAG_CODES

with open('oag_codes.json') as f:
   data = json.load(f)
print (data)

dictlist=[]
for i in data:    
    temp = [list(i.keys())[0],list(i.values())[0]]
    dictlist.append(temp)
oag_codes=pd.DataFrame(dictlist)


##### 2.	identify_codes.json

