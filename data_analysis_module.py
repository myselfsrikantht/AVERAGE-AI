#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
import statistics
from collections import Counter
from scipy.stats import skew

def analyze_data(numbers):
    numbers = [float(num) for num in numbers]

    num = len(numbers)
    mean = sum(numbers) / len(numbers)
    median = statistics.median(numbers)
    data_counter = Counter(numbers)
    modes = data_counter.most_common()
    skewness = skew(numbers)
    mean = np.mean(numbers)
    std_dev = np.std(numbers)
    z_scores = [(x - mean) / std_dev for x in numbers]
    
    if num <= 50:
        shapiro_test_stat, shapiro_p_value = stats.shapiro(numbers)
        if shapiro_p_value > 0.05:
            return "The mean of the data is: " + str(mean)
        elif -0.5 <= skewness >= 0.5:
            return "The median of the data is: " + str(median)
        elif any(z > 2 for z in z_scores):
            return "The median of the data is (Out): " + str(median)
        elif modes[0][1] > 1:
            return f"The mode of the data is: {modes[0][0]}"
        else:
            return "Finally, The mean of the data is: " + str(mean)
        
    elif num > 50:
        ks_stat, ks_p_value = stats.kstest(numbers, 'norm')
        if ks_p_value > 0.05:
            return "The mean of the data is: " + str(mean)
        elif -0.5 <= skewness >= 0.5:
            return "The median of the data is: " + str(median)
        elif any(z > 2 for z in z_scores):
            return "The median of the data is (Out): " + str(median)
        elif modes[0][1] > 1:
            return f"The mode of the data is: {modes[0][0]}"
        else:
            return "Finally, The mean of the data is: " + str(mean)
        
    else:
        return "For this given data, average could not be calculated"

