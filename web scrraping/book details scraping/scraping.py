import requests 
from bs4 import BeautifulSoup
import time
import pandas as pd


base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

page = 1 
while True :
    if page == 1 :
        url = "https://books.toscrape.com/"
    else :
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping page {page} .... ")

    response = requests.get(url , headers=headers)
    if response.status_code != 200 :
        print("NO MORE PAGES TO SCRAPE OR AN ERROR OCCURED")
        break

    soup = BeautifulSoup(response.text , "html.parser")
    books = soup.select(".product_pod")

    if not books :
        print("ALL PAGES ARE SCRAPED SUCCESSFULLY")
        break

    for book in books :
        title_tag = book.select_one("h3 a")
        title = title_tag.get("title" ) or title_tag.get_text(strip=True)
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)
        rating_tag = book.select_one(".star-rating")
        rating = [c for c in rating_tag["class"] if c != "star-rating"][0]
        link = "https://books.toscrape.com/catalogue/" + title_tag["href"]

        all_books.append({
            "Title" : title,
            "Price" : price,
            "Availability" : availability,
            "Rating" : rating,
            "URL" : link 
        })

    time.sleep(1)
    page += 1


df = pd.DataFrame(all_books)
df.to_csv("all_books.csv" , index=False , encoding="utf-8-sig")

print(f" SAVED {len(df)} books to all_books.csv ")
