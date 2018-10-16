#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:08:02 2018

@author: frank-lsy
"""

import re
import sh

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
    p = re.compile('\n')
    q = re.compile('\*')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    #print(arr)
    return arr

hla_a_arr = strip(hla_a_arr)
hla_b_arr = strip(hla_b_arr)
hla_c_arr = strip(hla_c_arr)

new_cin = strip(cin_arr)
new_gs = strip(gs_arr)
new_ebv = strip(ebv_arr)
new_msi = strip(msi_arr)

tumor_types = ['gs','ebv','cin','msi']
tumor_ids = {tumor_types[0]:new_gs,tumor_types[1]:new_ebv,tumor_types[2]:new_cin,tumor_types[3]:new_msi}
hla_types = ['A','B','C']
hla_ids = {hla_types[0]:hla_a_arr,hla_types[1]:hla_b_arr,hla_types[2]:hla_c_arr}

for tumor_type in tumor_types:
    for tumor_id in tumor_ids[tumor_type]:
        for hla_type in hla_types:
            for hla_id in hla_ids[hla_type]:
                input_file = "../qualified-tumor/{0}/{1}/{2}-qualified.csv".format(tumor_type,tumor_id,hla_id)
                output_dir = "../hla/{0}/{1}".format(hla_id,tumor_type)
                sh.mkdir("-pv",output_dir)
                output_file = "../hla/{0}/{1}.csv".format(output_dir,tumor_id)
                try:
                    f = open(input_file,'r')
                    sh.cp(input_file,output_file)
                    f.close()
                except FileNotFoundError:
                    print('NO SUCH FILE!{}'.format(input_file))