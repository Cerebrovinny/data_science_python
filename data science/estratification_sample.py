# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:51:36 2020

@author: Windows
"""

import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
#count selected class
iris['class'].value_counts()

#separete 25 samples of each item
X, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                     test_size = 0.5, stratify = iris.iloc[:,4]) #iloc function is to select specific parts of databse

y.value_counts()

infert = pd.read_csv('infert.csv')
infert['education'].value_counts()

X1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1],
                                test_size = 0.6, stratify = infert.iloc[:, 1])

y1.value_counts()