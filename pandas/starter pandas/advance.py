import pandas as pd

# data = {
#     "name" : ['sourav' , 'srishti' , 'sid' , 'sakshi'],
#     "age" : [21 , 23 , 25 , 25],
#     "city" : ['mumbai' , 'mumbai' , 'pune' , 'nagpur']
# }

# df = pd.DataFrame(data)
# print(df.loc[df['city'] == 'mumbai'])
# print(f" THE STUDENTS ABOVE 24 ARE : \n{df[df['age'] > 24]}")

#   multi indexing

arrays = [
    ['Europe', 'Europe', 'Asia', 'Asia'],
    ['France', 'Germany', 'China', 'Japan']
]

index = pd.MultiIndex.from_arrays(arrays , names=('Continent' , 'Country'))

data = {'GDP': [2700, 3800, 14000, 5000], 'Population': [65, 83, 1400, 126]}

df= pd.DataFrame(data , index = index)
# print(df)


# print(df.loc['Europe'])
# print(df.loc[('Asia','Japan'), 'GDP'])


# .xs() means cross section . It’s a shortcut to select data at a particular level of a MultiIndex.

print(df.xs("Europe"))
print(df.xs("GDP" , axis=1))

# INDEXSLICE 

idx = pd.IndexSlice
df.loc[idx['Europe', :], :]   # All countries in Europe
df.loc[idx[:, 'Japan'], :]    # Only Japan (from any continent)


print(df.query('Population > 100'))

df_unstacked = df.unstack(level='Country')
print(df_unstacked)