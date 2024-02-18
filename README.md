# Specification for Project 7 Applied Data Analytics

## Overview

Project 7 is a chance to explore applied data analytics, offering a preliminary introduction to more advanced topics in the field.
This project offers a guided introduction to several key areas in data analytics. It's an opportunity to apply your skills and try an area that you might enjoy.  Many of these areas are covered in more depth in subsequent courses.

You have the flexibility to choose from several application areas, each offering a glimpse into different aspects of data analytics:

1. ML. Basic Machine Learning (ML): Explore fundamental ML concepts using Python's statistical and visualization libraries with simple linear regression and predictive analytics.

1. App. Interactive Analytics App using Shiny for Python: Get introduced to creating interactive web applications with Shiny for Python. This choice focuses on building basic interactive tools for data analysis.

Later (or propose a project):

1. SQL. Applied SQL Project: Engage in an applied SQL project integrating Python and SQLite. This option focuses on database interactions and SQL for data manipulation and querying.

1. NLP. Web Mining and Natural Language Processing (NLP): Delve into the basics of web mining and NLP using Python's NLTK library. This area will allow you to explore text processing and extraction of information from web sources.

Each of these areas represents a critical component of data analytics, and this project guides you through applying these concepts in a practical setting.
The goal is not mastery; it's to gain a basic understanding and appreciation of their role and potential in the field of data analytics and learn where you might want to focus your efforts in the future.

The specification is similar to early projects, but you'll need to tailor it to your chosen area.

1. Will you use a Jupyter Notebook or a Python script?
2. What tools and libraries will you use?
3. What dependencies will you need to install in your project virtual environment?
4. How will you organize your project?
5. How will you manage your project with Git?
6. How will you document your tools, process, code, and project?

## Create a new GitHub repository with a README.md and a code file with the specified name.

- GitHub Repository:  datafun-07-ml
- GitHub Repository Url: https://github.com/Keyoungg2/datafun-07-ml
- Documentation:      README.md
- Source:             young_applied.ipynb

## Version Control with Git

Use Git for version control.
Document your workflow for managing the project in your README.md.

## Objective

Explore an area of applied data analytics.
Incorporate logging to document the process and provide feedback.

## Requirements

### 1. Environment Setup

1. Create and activate a project virtual environment.
1. Install all required packages into your local project virtual environment.
1. After installing the required dependencies, generate a requirements.txt file.
1. Document the process and commands you used in your README.md.
1. Add a .gitignore file to your project with useful entries.

### 2. Project Start

1. Create a docstring or markdown cell with a brief introduction to your project.
1. Include the usual introduction information.

### 3. Import Dependencies

Import the required dependencies, following the conventional order.

### 4. Logging

Logging is recommended for all script and notebook projects.
Implement logging to enhance debugging and maintain a record of program execution.

1. Configure logging to write to a file named log.txt.
1. Log the start of the program using logging.info().
1. Log the end of the program using logging.info().
1. Log exceptions using logging.exception().
1. Log other major events using logging.info().
1. Log the start and end of major functions using logging.debug().

### 5. Sections based on your choice of Applied Data Analytics

Sections choice for this project is Machine Learning (ML). See specs below area depending on your choice
and the specification details provided in their own document:

1. [Intro to Machine Learning](ML.md)
1. [Intro to Interactive Apps](APP.md)

## Code Design

### 6. Data Acquisition

Load the Seaborn tips dataset like we did the iris dataset.

```python
import seaborn as sns
import pandas as pd

# Load data into DataFrame
df = sns.load_dataset('tips')

```

### 7. Basic Data Exploration

First, use pandas to perform the basic data exploration tasks as the initial steps of
any data analysis project:

1. Load Data into DataFrame
2. Inspect Data w/head(), shape, and dtypes
3. Describe Summary Statistics
4. Display Histograms for Numeric Columns

For example:

```python
import pandas as pd
import matplotlib.pyplot as plt

# earlier loading.... 

# Inspect data with head(), shape, and dtypes
print(df.head(10))
print(df.shape)
print(df.dtypes)

# Describe summary statistics
print(df.describe())

# Display histograms for numeric columns
df.hist(figsize=(10, 8))
plt.show()
```

### 8. Data Visualization

Create a scatter chart of total bill amount vs tip amount.
For example:
  
```python
# Create scatter chart of total bill amount vs tip amount
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Tip vs Total Bill')
plt.show()
```

### 9. Model Building

Build a simple linear regression model to predict tip amount based on total bill amount.

Use the SciPy stats module linregress function to calculate slope and intercept for the best fit line through the data.

Redraw the scatter chart with the best fit line. 

Use the line equation (model) to predict tip amount for a total bill amount of $50.00.

Draw this point on the chart. 

For example:

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# ... initial EDA ....

# ... initial scatter chart... 

# Build a simple linear regression model to 
# predict tip amount based on total bill amount
# lingress() returns a tuple that includes the 
# slope and intercept for the best fit line
# as well as other statistical measures
slope, intercept, r_value, p_value, std_err = stats.linregress(df['total_bill'], df['tip'])

# Display the results of the model
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
print(f"P-value: {p_value}")
print(f"Standard Error: {std_err}")

# Discuss the results - is this a good model?
# How do you know? Use numbers, be specific. 

# Redraw the scatter chart with the best fit line
sns.scatterplot(x='total_bill', y='tip', data=df)

# Use the line equation (model) to predict tip amount 
# for a total bill amount of $50.00
x = 50
y = slope * x + intercept

# Draw this point on the chart
plt.scatter(x, y, color='red')
plt.show()


# Discuss the results - is this a good prediction?
# How do you know? Why or why not? Use numbers, be specific. 
```

### 10. Storytelling and Presentation

Interpret the process and results to craft a narrative around your findings.
Add additional visualizations around the independent (bill amount) and dependent variable (tip amount).
Consider questions such as:

- "Does the model have any limitations?"
- "How could the model be improved?"
- "Are there any potential biases or factors not accounted for in the model?"

Present your findings in a logical and engaging manner.

## Model Validation

The following metrics are used to evaluate the performance of a linear regression model.

R-squared (Coefficient of Determination)

This statistic provides an indication of the goodness of fit of a set of predictions to the actual values.
In simple terms, it represents how well the independent variable (total bill) explains the variability in the dependent variable (tip).
An R-squared value closer to 1 indicates a model that explains a large portion of the variance in the dependent variable.

P-value

This value helps you determine the statistical significance of your model coefficients. A low p-value (typically ≤ 0.05) indicates that you can reject the null hypothesis, which states that the coefficient is equal to zero (no effect).

Standard Error

This statistic measures the average amount that the estimated coefficients differ from the actual average value of our response variable. A lower standard error of the coefficient suggests more precise estimates.

```python
print(f"R-squared: {r_value**2}")
print(f"P-value: {p_value}")
print(f"Standard Error: {std_err}")
```

## 11. Code Structure and Documentation

Once the code runs without errors, focus on how the content is structured and documented.
Organize your code into well-defined sections, each with a clear purpose and header.
Provide context, explain your analysis, and share findings.
Make your code file informative and engaging.
Use comments and text to explain the purpose and functionality of the code, especially complex or non-obvious code segments.

## 12. Code Execution

Run your code to ensure it executes without errors.
Verify all code runs and visualizations render as expected.
Confirm that your code renders well on GitHub, so your work is accessible to others.

If working in a script, use conditional logic to ensure the script only runs
when executed directly and execute a main() function that contains the program logic.
