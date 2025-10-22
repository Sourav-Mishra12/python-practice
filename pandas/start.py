import pandas as pd

print(pd.__version__)


# SERIES --> A pandas 1- dimensional labeled array that can hold any data type . Think of it like a single column in a spreadsheet (1-dimensional)

data = [100,200,300,400,500]
series = pd.Series(data , index = ["a","b","c","d","e"]) 
 # the Series here is a constructor , not a function

print(series)
print(series.loc["a"])  # for accessing the location by the label
print(series.iloc[0])  # for accessing the integer location
print(series[series>=200])

calories = {"day1" : 1750,"day2":2000,"day3":3000,"day4":2050}
series = pd.Series(calories)
series.loc["day3"] += 500
print(series)

print(series[series == 2000])


