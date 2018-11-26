# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 03:32:04 2018

@author: himansh
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 01:39:32 2018

@author: himansh
"""
#from  pdftables.pdf_document import *
from pdfminer.pdfparser import *

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import  PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
#p=r'G:\\shipmnts\\AICST\\AICST\\MF\\HAWB\\235699-AWBLayout_305620180102155940-Page(3).pdf'
def convert_to_text(p):
    document = open('G:\\shipmnts\\AICST\\AICST\\MF\\HAWB\\'+p, 'rb')
    #Create resource manager
    rsrcmgr = PDFResourceManager()
    # Set parameters for analysis.
    laparams = LAParams()
    # Create a PDF page aggregator object.
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(document):
        interpreter.process_page(page)
        # receive the LTPage object for the page.
        layout = device.get_result()
        file=p[:-3]+"txt"
        for element in layout:
            if isinstance(element, LTTextBoxHorizontal):
                
                text_file = open("HAWB\\"+file, "a")
                text_file.write("%s" % element.get_text())
                
                print(element.get_text())
import os
for i in os.listdir("G:\\shipmnts\\AICST\\AICST\\MF\\HAWB\\"):
    try :convert_to_text(i)
    except : continue