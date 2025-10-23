import numpy as np 
import pandas as pd

df = pd.read_csv("SuperMarket Analysis.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
df['date'] = pd.to_datetime(df['date'])
df['hour'] = pd.to_datetime(df['time']).dt.hour


#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

# analyzing which branch has the highest sales

branch_sales = df.groupby('branch')['sales'].sum().sort_values(ascending=False)
#print(branch_sales)

# GIZA BRANCH IS HAVING THE MOST SALES OF 110568.7065

# analyzing which product is being sold the most

product_sales = df.groupby('product_line')['sales'].sum().sort_values(ascending=False)
#print(product_sales)

# FOOD AND BEVERAGES are being sold the most


# which payment method is being used the most

payment_methods = df['payment'].value_counts()
#print(payment_methods)

# EWALLETS are being used the most

# checking the average ratings of each branch
ratings_per_branch = df.groupby('branch')['rating'].mean().sort_values(ascending=False)
#print(ratings_per_branch)
# GIZA has the highest ratings in all of them

#checking the sales per day

sales_by_days = df.groupby('date')['sales'].sum().sort_values(ascending=False)
#print(sales_by_days)

sales_by_hour = df.groupby('hour')['sales'].sum()
print(sales_by_hour)

