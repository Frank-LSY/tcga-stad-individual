#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:45:12 2018

@author: frank-lsy
"""
import re

cin = open('../../tcga-stad/new/1-new.csv','r')
gs = open('../../tcga-stad/new/2-new.csv','r')
ebv = open('../../tcga-stad/new/3-new.csv','r')
msi = open('../../tcga-stad/new/4-new.csv','r')

cin_arr = cin.readlines()
gs_arr = gs.readlines()
ebv_arr = ebv.readlines()
msi_arr = msi.readlines()

cin.close()
gs.close()
ebv.close()
msi.close()

def strip(arr):
    p = re.compile('\n')
    q = re.compile('\*')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    #print(arr)
    return arr

def average(arr):
    tmp = 0
    for item in arr:
        tmp += item
    avg = tmp/len(arr)
    return avg

new_cin = strip(cin_arr)
new_gs = strip(gs_arr)
new_ebv = strip(ebv_arr)
new_msi = strip(msi_arr)

tumor_types = ['cin','ebv','gs','msi']
tumor_ids = {tumor_types[0]:new_cin,tumor_types[1]:new_ebv,tumor_types[2]:new_gs,tumor_types[3]:new_msi}

for tumor_type in tumor_types:
    output_file = "../average-qualified-lines/{0}.csv".format(tumor_type)
    avg_arr = []
    for tumor_id in tumor_ids[tumor_type]:
        input_file = "../qualified_lines/{0}/{1}.csv".format(tumor_type,tumor_id)
        f = open(input_file,'r')
        file = f.readlines()
        f.close()
        new_file = strip(file)
        new_file = list(map(float,new_file))
        avg = average(new_file)
        avg_arr.append(str(avg)+'\n')
    g = open(output_file,'a+')
    g.write(tumor_type+'\n')
    print(avg_arr)
    g.writelines(avg_arr)
    g.close()
    
        