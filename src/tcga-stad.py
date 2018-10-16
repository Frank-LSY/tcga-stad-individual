#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:37:29 2018

@author: frank-lsy
"""
import re
import sys
import csv
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver

MAX_CIN = 20
MAX_GS = 22
MAX_EBV = 17
MAX_MSI = 13

raw_url = "http://compbio-research.cs.brown.edu/public/stad/#!/"
gs="STAD-SCNAL-FREQ0P-D96/"
cin="STAD-CIN-FREQ2P-D93/"
ebv="STAD-EBV-FREQ0P-D82/"
msi="STAD-MSIH-FREQ2P-D30/"

#url = "http://compbio-research.cs.brown.edu/public/stad/#!/STAD-MSIH-FREQ2P-D30/1"

facet = [cin,gs,ebv,msi]
max_arr = [MAX_CIN,MAX_GS,MAX_EBV,MAX_MSI]

for k in range(4):
    mid_url = raw_url+facet[k]
    real_max = max_arr[k]
    with open('tcga-stad/'+str(k+1)+'.csv','w') as new:
        fieldnames = ["ID"]
        print("writing the "+str(k+1)+"th file")
        csvwriter = csv.DictWriter(new,fieldnames = fieldnames)   
        csvwriter.writeheader()
        new.close()
    
    i = 1    
    while (i<real_max+1):
        real_url = mid_url+str(i)
        print(real_url)
        
        driver=webdriver.Chrome()
        driver.get(real_url)
        delay = random.randint(5,15) #延时调整,网好调快一点，网不好慢一点
        time.sleep(delay)
        r = driver.page_source
        soup=BeautifulSoup(r,'html.parser')
        driver.close()
        
        mid = re.findall(r'TCGA-[A-Z0-9][A-Z0-9]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]',str(soup))    
      
        j = 0
        result = []
    
        while  (j<len(mid)):
            result.append(mid[j])
            j = j+2
        
        print(result)
        if (len(result)==0):
            print("again")
            continue
         
        with open('tcga-stad/'+str(k+1)+'.csv','a+') as new:
            fieldnames = ["ID"]
            print("finish writing the "+str(i)+"th sample")
            csvwriter = csv.DictWriter(new,fieldnames = fieldnames)   
            for item in result:
                csvwriter.writerow({"ID":item})
            new.close()
        i += 1        