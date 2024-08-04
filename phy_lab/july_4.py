import numpy as np  
import pandas as pd  
import math
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

Data=[165, 150, 125, 120,150, 150, 140, 145, 120, 150]
Data=np.array(Data)
# mean 
mean=np.mean(Data)
# variance 
variance=np.var(Data)
# standard deviation 
std_dev=np.std(Data,ddof=0)
# minimum, maximum
max_value=np.max(Data)
min_value=np.min(Data)
# quartile 1, quartile 3
q1=np.percentile(Data,25)
q3=np.percentile(Data,75)
# mean deviation and mode of the following heart rates for ten asthmatic patients in a state of respiratory arrest
avg_deviation=np.mean(np.abs(Data-mean))
print(mean,variance,std_dev,max_value,min_value,q1,q3,avg_deviation)

#141.5 205.25 14.326548781894402 165 120 128.75 150.0 12.2