from scipy.stats import norm
from scipy import stats
import matplotlib.pyplot as plt

# set of objects in basket, media is 8 and standard deviation
# is 2 whats the prob of take an object with the wheight is less then 6 kg

norm.cdf(6, 8, 2)

#what the prob of take object is + then 6kg
norm.sf(6, 8, 2)
1 - norm.sf(6, 8, 2)

# prob of take an object -6 or +10 kg
norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

# prob of take an object -10 and + 8kg
norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)

data = norm.rvs(size = 100)
stats.probplot(data, plot = plt)

stats.shapiro(data)