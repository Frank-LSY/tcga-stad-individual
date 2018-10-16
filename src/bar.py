#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:53:24 2018

@author: frank-lsy
"""

import matplotlib.pyplot as plt
import pandas as pd

cin = pd.read_csv("../bar/cin.csv")
ebv = pd.read_csv("../bar/ebv.csv")
gs = pd.read_csv("../bar/gs.csv")
msi = pd.read_csv("../bar/msi.csv")
#print(bar["HLA"]) 
name_list = cin["HLA"]
cin_list = cin["Amounts"]
ebv_list = ebv["Amounts"]
gs_list = gs["Amounts"]
msi_list = msi["Amounts"]

'''
plt.bar(name_list,cin_list,label = "cin",fc='r')
plt.legend()
plt.savefig("../bar-cin.png",dpi = 2560)
plt.show()
'''
'''
plt.bar(name_list,ebv_list,label = "ebv")
plt.legend()
plt.savefig("../bar-ebv.png",dpi = 2560,fc='y')
plt.show()
'''

plt.bar(name_list,gs_list,label = "gs",fc='g')
plt.legend()
plt.savefig("../bar-gs.png",dpi = 2560)
plt.show()


plt.bar(name_list,msi_list,label = "msi",fc = '#ffff00',width = 0.5)
plt.legend()
plt.savefig("../bar-msi.png",dpi = 2560)
plt.show()
