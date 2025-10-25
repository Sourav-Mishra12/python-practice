import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("client_sales_data.csv")
print(df)
#print(df.info())
#print(df.describe())
#print(df.dtypes)


# analyze the data and tell the key sales insights
# visualize them (charts preffered)
# write a small summary i can use in my internal team meeting

# focus on sales trends,top cities,top products and categories
# also analyze and report anything interesting in customer patterns

# analyzong which product brings the most revenue
highest_revenue = df.groupby('Product')['TotalAmount'].sum().sort_values(ascending=False)
#print(highest_revenue)

# the table lamp holds the highest revenue for you , which is about 6500 ruppess and the lowest is the ceramic vase which is 800 , so we can see a very big difference between the top and the bottom

highest_category = df.groupby('Category')['TotalAmount'].sum().sort_values(ascending=False)
#print(highest_category)

# we can see a very good demand for the lighting category with total revenue of 8100 whhich also adds upto our previous analysis about the highest revenue generating product

highest_city = df.groupby('City')['TotalAmount'].sum().sort_values(ascending=False)
#print(highest_city)

# delhi is the city where most of the revenue lies in its about 6500 rupees

grouped = df.groupby(['Product','City'])['TotalAmount'].sum().reset_index()
#print(grouped)

best_products = grouped.loc[grouped.groupby('City')['TotalAmount'].idxmax()]
print(best_products)