# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')

sample1 = np.random.choice(a = [0, 1], size = 150, replace = True,
                           p = [0.5, 0.5])#this addtion need to result in total (1) #if false and already selected the option can't be selected again
#select item and type (command or ctrl + u+i to show help menu)