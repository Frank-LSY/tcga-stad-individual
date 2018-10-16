#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:23:15 2018

@author: frank-lsy
"""
import os

facets=["cin/","ebv/","gs/","msi/"]

general_input_dir = "../filter/" 
general_output_dir = "../single/"
for i in range(4):
    input_dir = general_input_dir+facets[i]
    output_dir = general_output_dir+facets[i]
    files = os.listdir(input_dir)
    for file in files:
        with open(input_dir+file,'r') as reader, open(output_dir+file, 'w') as writer:
            for line in reader:
                items = line.strip().split()
                print(' '.join(items[:10]), file=writer)