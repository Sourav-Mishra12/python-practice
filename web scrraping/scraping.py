import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://quotes.toscrape.com/page/{}/"

all_quotes = []

for page in range(1,11):
    url = base_url.format(page)
    response = requests.get(url)
    if response.status_code != 200 :
        print("FETCHING FAILED ")
        break 

    soup = BeautifulSoup(response.text , "html.parser")

    for q in soup.select(".quote"):
        text = q.select_one(".text").get_text(strip=True)
        author = q.select_one(".author").get_text(strip=True)
        tags = [tag.get_text() for tag in q.select(".tags .tag")]
        all_quotes.append({
            "quotes" : text,
            "Author" : author,
            "Tags" : ", ".join(tags)
        })


df = pd.DataFrame(all_quotes)
df.to_csv("quotes.csv" , index=False)
print("saved " , len(df) , "quotes to quotes.csv")

