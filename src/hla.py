#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:20:00 2018

@author: frank-lsy
"""
from mhcnuggets.src.predict import predict
import re
import os
import sh
import gc
import resource
import time
import psutil
import tracemalloc

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
#print (hla_a_arr)
#print (hla_b_arr)
#print (hla_c_arr)

def pre(hla_arr,input_dir,output_dir):
    #pid = os.getpid()
    #p = psutil.Process(pid)
    #print ('Process info:')
    #print ('name: ', p.name())
    #print ('exe:  ', p.exe())

    files = os.listdir(input_dir)
    for file in files:
        output_file = '{0}{1}'.format(output_dir,file)
        input_file = '{0}{1}'.format(input_dir,file)
        sh.mkdir(output_file)
        for item in hla_arr:
            start = time.time() 
            tracemalloc.start(10)   
            predict(class_='I',
                    peptides_path= input_file, 
                    mhc=item,output ='{0}{1}/{2}.csv'.format(output_dir,file,item))
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('traceback')
            end = time.time()
            stat = top_stats[0]
            #print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
            #for line in stat.traceback.format():
            #    print(line)
            print(end-start)
            #info = p.memory_full_info()
            #memory = info.uss / 1024. / 1024.
            #print ('Memory used: {:.2f} MB'.format(memory))
    #resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        
#pre(hla_a_arr,"../pep/cin/","../predict/cin/")
#pre(hla_b_arr,"../pep/cin/","../predict/cin/")
#pre(hla_c_arr,"../pep/cin/","../predict/cin/")

pre(hla_a_arr,"../pep/ebv/","../predict/ebv/")
pre(hla_b_arr,"../pep/ebv/","../predict/ebv/")
pre(hla_c_arr,"../pep/ebv/","../predict/ebv/")

#pre(hla_a_arr,"../pep/gs/","../predict/gs/")
#pre(hla_b_arr,"../pep/gs/","../predict/gs/")
#pre(hla_c_arr,"../pep/gs/","../predict/gs/")

#pre(hla_a_arr,"../pep/msi/","../predict/msi/")
#pre(hla_b_arr,"../pep/msi/","../predict/msi/")
#pre(hla_c_arr,"../pep/msi/","../predict/msi/")
