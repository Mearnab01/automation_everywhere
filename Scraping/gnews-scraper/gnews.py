import requests
from bs4 import BeautifulSoup

def get_results(term, count):
    results = []
    url = f'https://news.google.com/rss/search?q={term}&hl=en-US&gl=US&ceid=US:en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    items = soup.find_all('item')[:count]

    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        results.append((title, link))

    return results

user_input= input("Enter a term to scrape news from Google: ")


items = get_results(user_input, 5)
for title, link in items:
    print(f"Title: {title} - {link} ","\n")
