#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:46:23 2018

@author: frank-lsy
"""
for i in range(4):
    new = []
    with open ('tcga-stad/'+str(i+1)+'.csv','r') as file:
        for line in file.readlines():
            new.append(line)
        #print(new)
        txt = list(set(new))
        txt.sort(key = new.index)
        print(len(txt))
        print(txt)
    f = open('tcga-stad/new/'+str(i)+'-new.csv','w')
    f.writelines(txt)