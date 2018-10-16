#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 10:03:24 2018

@author: frank-lsy
"""

import matplotlib.pyplot as plt
import pandas as pd
import csv

hla = pd.read_csv("../dataset/HLA-all.csv")
#print(hla)
tmp = open("../dataset/HLA-all.csv",'r')
reader = csv.DictReader(tmp)
class_list = [row['Class'] for row in reader]
name_list = hla["Type"]
hla_list = hla["Frequency"]
print(class_list)
plt.legend()
for i in range(len(class_list)):
    plt.gca().invert_yaxis()
    plt.bar(name_list[i],hla_list[i], fc = class_list[i],width = 0.5)
plt.savefig("../hla-frequency.png",dpi = 2560)
plt.show()