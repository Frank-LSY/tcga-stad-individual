#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:19:49 2018

@author: frank-lsy
"""
import re


def extract(input_file,source_arr,output_dir):
    head = "Amounts,HLA,Type\n"
    for item in source_arr:
        f = open(input_file,'r')
        line_num = 0
        g = open(output_dir+item+".csv",'a+')
        g.writelines(head)
        #print("writing the "+item+" file.")
        while 1:
            line_num += 1
            line = f.readline()
            #print(line)
            #print (item)
            t = re.findall(r''+item,line)
            if (t):
                #print(item)
                #print(line_num)
                g.writelines(line)
            if not line:
                break
        f.close()
    g.close()
    
    
    
input_file = "../hla.csv"
output_dir = "../bar/"
facets = ["cin","ebv","gs","msi"]

extract(input_file,facets,output_dir)