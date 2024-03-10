# AVERAGE-AI
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AVERAGE AI</title>
</head>
<body>

    <h1>Introduction:</h1>
    <p>If the user inputs data, the program calculates the appropriate average using the mean, median, and mode.</p>

    <h1>Methods & Models:</h1>

    <h2>Mean:</h2>
    <p>Formula: Mean = (Sum of all values) / (Number of values)</p>

    <h2>Median:</h2>
    <p>The median is the middle value of a dataset when it is ordered.</p>
    <p>For an odd number of observations, the median is the middle value.</p>
    <p>For an even number of observations, the median is the average of the two middle values.</p>

    <h2>Mode:</h2>
    <p>The mode is the value that appears most frequently in a dataset.</p>
    <p>A dataset may have no mode, one mode (unimodal), or more than one mode (multimodal).</p>

    <h2>Skewness:</h2>
    <p>Skewness measures the asymmetry of a probability distribution.</p>
    <p>Positive skewness indicates a longer right tail, while negative skewness indicates a longer left tail.</p>
    <p>Formula for sample skewness: Skewness = (n / (n-1)(n-2)) * Σ((Xi - X̄) / s)^3</p>

    <h2>Shapiro-Wilk Test:</h2>
    <p>The Shapiro-Wilk test is used to assess the normality of a dataset.</p>
    <p>Null hypothesis: The data follows a normal distribution.</p>
    <p>The test statistic is calculated, and p-value is compared to a significance level.</p>
    <p>If p-value is less than the chosen significance level, the null hypothesis is rejected.</p>

    <h2>Kolmogorov-Smirnov Test:</h2>
    <p>The Kolmogorov-Smirnov test assesses the goodness of fit between the observed distribution and a theoretical distribution.</p>
    <p>It is often used to test whether a sample is drawn from a specific distribution.</p>
    <p>The test statistic is calculated based on the maximum vertical distance between the empirical distribution function and the theoretical distribution function.</p>

    <h1>Procedure:</h1>

    <h2>First Part:</h2>
    <p>If the input observation size is less than 50:</p>
    <ul>
        <li>If the p-value of the Shapiro-Wilcoxon test is greater than 0.05 (indicating a normal distribution), the model prints the mean.</li>
        <li>Else if the skewness value falls within the range of -0.5 to 0.5, the model prints the median.</li>
        <li>Otherwise, it prints the mode.</li>
    </ul>

    <h2>Second Part:</h2>
    <p>If the data size is greater than 50:</p>
    <ul>
        <li>If the p-value of the Kolmogorov-Smirnov test is greater than 0.05 (indicating a normal distribution), the model prints the mean.</li>
        <li>Else if the skewness value falls within the range of -0.5 to 0.5, the model prints the median.</li>
        <li>Otherwise, it prints the mode.</li>
    </ul>

    <h1>Conclusion:</h1>
    <p>When the user inputs the data:</p>
    <p>100 -26 131 306 -46 -46 317 154 -93 110</p>
    <p>Then the result will be, If the given data follows a normal distribution, the model outputs: 'The mean of the data is 90.7.' Otherwise, if the data is skewed, the output is: 'The median of the data is 105.' In this case, as there are no repeated values, there is no mode.</p>

</body>
</html>
