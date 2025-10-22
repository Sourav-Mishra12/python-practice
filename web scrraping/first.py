import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Find all book titles
books = [b.text for b in soup.find_all("h3")]
print(books)


# this is headache bruhhh i need some time to process until then byee