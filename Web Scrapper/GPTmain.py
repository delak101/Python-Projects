import requests
from bs4 import BeautifulSoup

def fetch_books(url):
    """Fetch the HTML content from the given URL and return the parsed BeautifulSoup object."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    return BeautifulSoup(response.content, "html.parser")

def extract_book_info(book):
    """Extract and return the title and rating of a book from the BeautifulSoup object."""
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    return title, rating

def display_books(books):
    """Print the title and rating of each book."""
    for book in books:
        title, rating = extract_book_info(book)
        print(f"- Book title: {title}\n  Rating: {rating}\n")

def main():  # sourcery skip: use-named-expression
    url = "https://books.toscrape.com/"
    soup = fetch_books(url)
    
    if soup:
        books = soup.find_all("article", class_="product_pod")
        display_books(books)

if __name__ == "__main__":
    main()
