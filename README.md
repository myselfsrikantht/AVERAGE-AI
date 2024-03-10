# AVERAGE-AI
# Introduction:

If the user inputs data, the program calculates the appropriate average using the mean, median, and mode.

# Methods & Models:

**Mean:**
Formula: Mean = (Sum of all values) / (Number of values)

**Median:**
The median is the middle value of a dataset when it is ordered.
For an odd number of observations, the median is the middle value.
For an even number of observations, the median is the average of the two middle values.

**Mode:**
The mode is the value that appears most frequently in a dataset.
A dataset may have no mode, one mode (unimodal), or more than one mode (multimodal).

**Skewness:**
Skewness measures the asymmetry of a probability distribution.
Positive skewness indicates a longer right tail, while negative skewness indicates a longer left tail.
Formula for sample skewness: Skewness = (n / (n-1)(n-2)) * Σ((Xi - X̄) / s)^3

**Shapiro-Wilk Test:**
The Shapiro-Wilk test is used to assess the normality of a dataset.
Null hypothesis: The data follows a normal distribution.
The test statistic is calculated, and p-value is compared to a significance level.
If p-value is less than the chosen significance level, the null hypothesis is rejected.

**Kolmogorov-Smirnov Test:**
The Kolmogorov-Smirnov test assesses the goodness of fit between the observed distribution and a theoretical distribution.
It is often used to test whether a sample is drawn from a specific distribution.
The test statistic is calculated based on the maximum vertical distance between the empirical distribution function and the theoretical distribution function.

# Procedure:

**First Part:**
If the input observation size is less than 50:

If the p-value of the Shapiro-Wilcoxon test is greater than 0.05 (indicating a normal distribution), the model prints the mean.
Else if the skewness value falls within the range of -0.5 to 0.5, the model prints the median.
Otherwise, it prints the mode.

**Second Part:**
If the data size is greater than 50:

If the p-value of the Kolmogorov-Smirnov test is greater than 0.05 (indicating a normal distribution), the model prints the mean.
Else if the skewness value falls within the range of -0.5 to 0.5, the model prints the median.
Otherwise, it prints the mode.

# Conclusion:

When the user inputs the data:
100 -26 131 306 -46 -46 317 154 -93 110
Then the result will be, If the given data follows a normal distribution, the model outputs: 'The mean of the data is 90.7.' Otherwise, if the data is skewed, the output is: 'The median of the data is 105.' In this case, as there are no repeated values, there is no mode.
