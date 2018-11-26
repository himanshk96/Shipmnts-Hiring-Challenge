# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 01:21:41 2018

@author: himansh
"""

import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    
    return text

#print (convert_pdf_to_txt('235699-AWBLayout_305620180102155940-Page(3)'))
import os
for i in os.listdir("G:\\shipmnts\\AICST\\AICST\\MF\\HAWB\\")[:9]:
    try:
        text=convert_pdf_to_txt(r'G:\\shipmnts\\AICST\\AICST\\MF\\HAWB\\'+i)
#print (convert_pdf_to_txt(r'G:\\shipmnts\\AICST\\AICST\\MF\\HAWB\\235699-AWBLayout_305620180102155940-Page(3).pdf'))
    
        filename=i[:-3]+"txt"
        text_file = open("HAWB2\\"+filename, "w")
        text_file.write("%s \n" % text)
        
        text_file.close()
    except: continue
    print(text)
