#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:50:59 2018

@author: frank-lsy
"""

import csv
import re
import os
import sh
IC50_THRESHOLD = 500

f = open('../pre/cin/TCGA-BR-4183.pep/A/HLA-A03:01\r.csv','r')
reader = f.readlines()

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
    p=re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
    #print(arr)
    return arr


def qualified_peptide(input_file,output_file):
    qualified_rows = []
    try:     
        with open(input_file,'r') as fileIn:
            file = csv.DictReader(fileIn)
            for row in file:
                if (float(row['ic50'])<=IC50_THRESHOLD):
                    rows = [row['peptide'],row['ic50']]
                    qualified_rows.append(rows)
    except FileNotFoundError:
        print('NO SUCH FILE!{}'.format(input_file))
            #print(qualified_rows)
    with open (output_file,'w') as fileOut:
        file = csv.writer(fileOut)
        for item in qualified_rows:  
            file.writerow(item)
        

tumor_types = ['cin','ebv','gs','msi']

new_cin = strip(cin_arr)
new_gs = strip(gs_arr)
new_ebv = strip(ebv_arr)
new_msi = strip(msi_arr)

tumor_ids = {tumor_types[0]:new_cin,tumor_types[1]:new_ebv,tumor_types[2]:new_gs,tumor_types[3]:new_msi}

hla_types = ['A','B','C']

hla_a_arr = strip(hla_a_arr)
hla_b_arr = strip(hla_b_arr)
hla_c_arr = strip(hla_c_arr)

hla_ids = {hla_types[0]:hla_a_arr,hla_types[1]:hla_b_arr,hla_types[2]:hla_c_arr}


for tumor_type in tumor_types:
    for tumor_id in tumor_ids[tumor_type]:
        for hla_type in hla_types:
            for hla_id in hla_ids[hla_type]:
                #input_file1 = '../normal/{0}/{1}/{2}-normal.csv'.format(tumor_type,tumor_id,hla_id)
                #output_dir1 = '../qualified-normal/{0}/{1}'.format(tumor_type,tumor_id)
                #sh.mkdir("-pv",output_dir1)
                #output_file1 = '{0}/{1}-qualified.csv'.format(output_dir1,hla_id)
                #qualified_peptide(input_file1,output_file1)

                input_file2 = '../tumor/{0}/{1}/{2}-tumor.csv'.format(tumor_type,tumor_id,hla_id)
                output_dir2 = '../qualified-tumor/{0}/{1}'.format(tumor_type,tumor_id)
                sh.mkdir("-pv",output_dir2)
                output_file2 = '{0}/{1}-qualified.csv'.format(output_dir2,hla_id)
                qualified_peptide(input_file2,output_file2)
    print(tumor_type+'finish!')
