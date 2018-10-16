#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 10:50:47 2018

@author: frank-lsy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#tips = sns.load_dataset("tips")
#print(tips)

grey = pd.read_csv('../lines/grey.csv')
red = pd.read_csv('../average-qualified-lines/red.csv')
final = pd.read_csv("../final.csv")
maybe = pd.read_csv("../maybe.csv")
columns=['cin','ebv','gs','msi']
#print (grey)

#color = dict()
#plt.style.use('ggplot')
"""
grey.plot.box(
              patch_artist=False,
              showmeans=True,
              widths = 0.5,
              #positions = [0.25,0.75,1.25,1.75],
              #boxprops = {'color':'black','facecolor':'white','linewidth':2},
              flierprops = {'marker':'o','markerfacecolor':'grey','color':'grey'},
              meanprops = {'marker':'o','markerfacecolor':'red'},
              medianprops = {'linestyle':'-','color':'red','linewidth':2},
              whiskerprops = {'linestyle':'--','color':'green'},
              capprops = {})


plt.yscale('log')
plt.ylabel("Amount")
plt.xlabel("Type")
plt.show()
"""
f = sns.boxplot(x="tumor_type",
                  y="lines",
                  hue="qualified",
                  data=maybe,
                  showmeans=True,
                  notch=False,
                  flierprops = {'marker':'o','markerfacecolor':'black','color':'darkred'},
                  meanprops = {'marker':'D','markerfacecolor':'darkgreen'},
                  medianprops = {'linestyle':'-','color':'darkred','linewidth':2},
                  whiskerprops = {'linestyle':'--','color':'green'})
"""
g = sns.swarmplot(x="tumor_type",
                  y="lines",
                  hue="qualified",
                  data=maybe)
"""
#plt.scatter(x = grey["cin"],y = grey["ebv"])
plt.yscale('log')
plt.ylabel("Amount")
plt.xlabel("Type")
plt.savefig("../box.png",dpi = 2560)
plt.show()

