import numpy as np
import pandas as pd
from math import ceil

population = 150
sample = 15
k = ceil(population / sample)

r = np.random.randint(low = 1, high = k + 1, size = 1)

acomulator = r[0]
winners = []
for i in range(sample):
    #print(acomulator)
    winners.append(acomulator)
    acomulator += k
    
base = pd.read_csv('iris_csv')
base_final = base.loc[winners]