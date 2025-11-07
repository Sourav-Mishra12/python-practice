from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("all_books.csv")
text = " ". join(df["Title"] . astype(str))

wordcloud = WordCloud(width=800,height=400,background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud , interpolation="bilinear")
plt.axis('off')
plt.title("MOST COMMON WORDS IN BOOK TITLES " , fontsize=16)
plt.show()