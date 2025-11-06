import pandas as pd
from itertools import chain
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("quotes.csv")

# EXPLORING THE DATA 

# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.shape)


# CHECKING FOR NULLS AND DUPLICATES

#print(df.isnull().sum()) # there were 3 null vales in the tags column
#print(df.duplicated().sum())  # found no duplicates in the data


# SPLITTING TAGS INTO LIST AS I WANT TO ANALYZE IT FURTHER

df["Tags"] = df["Tags"].fillna("").apply(lambda x : [t.strip() for t in x.split(",")] if isinstance(x,str) else [])

# ANALYSIS

print("TOP 10 AUTHORS BY THE NUMBER OF QUOTES\n")
print(df["Author"].value_counts().head(10))  # top 10 authors by no. of quotes

# most common tags overall the dataset

all_tags = list(chain.from_iterable(df["Tags"]))
tag_counts = pd.Series(all_tags).value_counts()

print("\nTOP 10 MOST COMMON TAGS ")
print(tag_counts.head(10))


# Average number of tags per quote

df["Tag_count"] = df["Tags"].apply(len)
print("Average number of tags used per quote : " , round(df["Tag_count"].mean()))


# checking which author uses the most tags on an average

author_tag_stats = df.groupby("Author")["Tag_count"].mean().sort_values(ascending=False)

print("\n THE TOP 10 AUTHOR WHO USES THE MOST TAGS ON AN AVERAGE\n")
print(author_tag_stats.head(10))


# which authors are most associated with life tag

# def has_tag(tag_list, tag_name):
#     return tag_name in tag_list

# df["has_life_tag"] = df["Tags"].apply(lambda x: has_tag(x, "life"))

# life_authors = (
#     df[df["has_life_tag"]]
#     ["Author"]
#     .value_counts()
#     .head(10)
# )
# print("Top authors with the 'life' tag:")
# print(life_authors)


# quick summary ones

print("UNIQUE AUTHORS : " , df["Author"].nunique())
print("UNIQUE TAGS : ", len(tag_counts) )
print("TOTAL QUOTES : ", len(df))



# VISUALISATION

sns.barplot(x=df["Author"].value_counts().head(10).values,
            y=df["Author"].value_counts().head(10).index)
plt.title("Top 10 Authors by Quotes")
plt.xlabel("Count")
plt.ylabel("Author")
plt.tight_layout()
plt.show()