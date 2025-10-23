import pandas as pd

print(pd.__version__)


# SERIES --> A pandas 1- dimensional labeled array that can hold any data type . Think of it like a single column in a spreadsheet (1-dimensional)

#data = [100,200,300,400,500]
#series = pd.Series(data , index = ["a","b","c","d","e"]) 
 # the Series here is a constructor , not a function

#print(series)
#print(series.loc["a"])  # for accessing the location by the label
#print(series.iloc[0])  # for accessing the integer location
#print(series[series>=200])

#calories = {"day1" : 1750,"day2":2000,"day3":3000,"day4":2050}
#series = pd.Series(calories)
#series.loc["day3"] += 500
#print(series)

#print(series[series == 2000])


# DATAFRAMES --> A tabular data structure with rows and columns .2-dimensional . Similar to an excel spreadsheet

data = {"NAME" : ["sourav","srishti","sakshi"],
        "AGE": [21 , 22, 24]
        }

df = pd.DataFrame(data , index = [1,2,3]) # dataframe here is a constructor

print(df)

# eveyrthing else for filtering is the same as series

# ADD A NEW COLUMN
df["MARKS"] = [77,87,92]
print(df)

# ADD A NEW ROW (we can add more rows just like making new dicts)

new_row = pd.DataFrame([{"NAME":"sidd","AGE":25,"MARKS":92}],index=[4])
df = pd.concat([df,new_row])
print(df)

# IMPORTING FILES SUCH AS CSV , JSON ,etc.

#df = pd.read_csv("fileName")  this is for csv
# print(df.to_string())  for displaying the whole data at once 

# df = pd.read_json("fileName")  this is for json

# SELECTION TECHNIQUES

# SELECTION BY COLUMN 
# print(df["name"]) pandas generally print the first 5 data and the last 5 data

# print(df[["name","height","age"]]) this is for accessing multiple columns

# SELECTION BY ROWS

# df = pd.DataFrame("filename" , index_col = "name") we did this so we can access any row by its name rather than index number for convenience
# print(df.loc["sourav"]) 
# print(df.loc["sourav" , ["height" , "age"]])
# print(df.loc("name1":"name99")) to select a range

# user = input("enter the name you want to find : ")
# try :
#       print(df.loc[user])
# except keyerror:
#       print(f"THE USER {user} not found")




# FILTERING

#tall_user = df[df[height >= 6 ]]
# everything is as same as NUMPY hehheheeee


# AGGREGATION 

# AGGREGATE FUNCTIONS --> they reduce a set of values into a single summary value , used to summarize and analyze data , often used with the groupby() function

# THIS WILL BE APPLIED TO THE WHOLE DATA FRAME

#print(df.mean(numeric_only = True))
#print(df.sum(numeric_only = True))
#print(df.min(numeric_only = True))
#print(df.max(numeric_only = True))
#print(df.count()) count won't include any null values

# single column

#print(df["age"].mean())
#print(df["height"].sum(numeric_only = True))
#print(df["height"].min(numeric_only = True))
#print(df["height"].max(numeric_only = True))
#print(df["height"].count(numeric_only = True))

# groupby()

# group = df.groupby("type1")
# print(group["height"].mean())

# we can multiple aggreagate functions in it


# DATA CLEANING

# the process of fixing / removing incomplete , incorrect or irrelevant data. 757 of work done with pandas is data cleaning

# df = df.drop(columns = ["height"]) this drops the columns

# df = df.dropna(subset = ["type2"])  to drop missing values

# df = df.fillna({"column_name":"replacing_name"})  to fill the missing values

# df["columnname"] = df["colname"].replace({"grass": "GRASS"}) # fix incosistent values

# df["name"]=df["name"].str.lower() standardize text

# df["salary"]=df["salary"].astype(bool)  # fix data types

# df = df.drop_duplicates()  to drop duplicates