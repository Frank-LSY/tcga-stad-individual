#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:15:24 2018

@author: frank-lsy
"""

import re
import csv

hla_a = open("../dataset/HLA-A.csv","r")
hla_b = open("../dataset/HLA-B.csv","r")
hla_c = open("../dataset/HLA-C.csv","r")

hla_a_arr = hla_a.readlines()
hla_b_arr = hla_b.readlines()
hla_c_arr = hla_c.readlines()

hla_a.close()
hla_b.close()
hla_c.close()

def strip(arr):
    p=re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
    #print(arr)
    return arr

hla_a_arr = strip(hla_a_arr)
hla_b_arr = strip(hla_b_arr)
hla_c_arr = strip(hla_c_arr)

hla_arr = hla_a_arr+hla_b_arr+hla_c_arr

#print(hla_arr)

def adjust(input_dir,output_file):
    g = open(output_file,"a+")
    fieldnames = ["Amounts","HLA","Type"]
    dict_writer = csv.DictWriter(g, fieldnames = fieldnames)
    dict_writer.writeheader()
    for i in range(len(hla_arr)):
        input_file = "{0}/{1}.csv".format(input_dir,hla_arr[i])
        f = open(input_file,'r')
        context = f.read()
        print(context)
        num = re.findall(r'\d+',context)
        amount = [num[0],num[3],num[6],num[9]]
        print(amount)
        hla = re.findall(r'HLA-[A-Z][0-9][0-9]:[0-9][0-9]',context)
        print(hla)
        facet = re.findall(r'(cin|ebv|gs|msi)',context)
        print(facet)
        for j in range(4):
            dict_writer.writerow({"Amounts":amount[j],"HLA":hla[j],"Type":facet[j]})
    g.close()    



input_dir = "../hla-lines"
output_file = "../hla.csv"
adjust(input_dir,output_file)