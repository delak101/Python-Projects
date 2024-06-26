import requests
from bs4 import BeautifulSoup
# website = input("Enter Website: ")

response = requests.get("https://books.toscrape.com/")

#soup = input("Enter soup: ")

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

print(books)