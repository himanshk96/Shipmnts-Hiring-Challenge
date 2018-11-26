# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 02:33:01 2018

@author: himansh
"""

import json
from pprint import pprint

with open('G:\shipmnts\code\document_labels.json') as f:
    data = json.load(f)

pprint(data)