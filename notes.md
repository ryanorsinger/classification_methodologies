# Classification

Primary goal of developing a classificaiton model is to generalize patters so we can determine the category/class of new data with a high degree of certainty

## Vocabulary
- Classifier - an algorithm that maps the input data to a specific category
- Classification model - a series of steps that take the pattners of input variables, generalize those patterns, and apply to new data in order to predict the class
- Feature - a feature aka input variable aka independent variable is an individual, measureable property of a phenomenon being observed
- Binary classification - Classification with only two outcomes like pass/fail, hotdog/hamburger, etc...
- Multiclass Classification - classification with more than two classes, like student letter grades

## Common Classification Algorithms
- Logistic Regression
- Decision Tree
- Naive Bayes
- K-Nearest Neighbors
- Random Forest
- Support Vector Machine
- Stochastic Gradient Descent
- AdaBoost
- Bagging
- GradientBoosting

## Binning
Summarize data in columns.

General rule of thumb:
- for all non-numeric type variables (object, category, boolean, e.g.), you will not use the bins argument.
- for numeric variables where the number of unique values is < 10, you will also not want to use the bins argument.
- for numeric variables where the number of unique values is >= 10, you will want to use the bins argument.
    
Options: (sort, bins, and dropna)
- `df.sex.value_counts()`
- `df.fare.value_counts(bins=10, sort=False)`
- `df.embark_town.value_counts(dropna=False)`
