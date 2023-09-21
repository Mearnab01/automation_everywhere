from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

def scrape(url): 
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful

        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print("Error fetching the page:", e)
        return None

product_names = []
product_prices = []
product_link=[]

def get_data(soup):
    try:
        box=soup.find("ul",class_="srp-results srp-list clearfix")

        titles = box.find_all('div', class_='s-item__title')
        prices = box.find_all('span', class_='s-item__price')
        links=box.find_all('div',class_="s-item__image")

        for title, price, link in zip(titles, prices, links):
            product_names.append(title.text)
            product_prices.append(price.text)
            product_link.append(f"{link.a['href']}")


    except AttributeError as e:
        print("Error extracting data:", e)


for page in range(1,11):
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw=books&_sacat=0&_ipg=240&_pgn={page}&rt=nc"
    soup = scrape(url)

    if soup:
        get_data(soup)

# Print the collected product names and prices for each page
for name, price, link in zip(product_names, product_prices, product_link):
    #print(f"Product Name: {name} | Price: {price} | {link}")
    pass

try:
    # Save data to CSV
    data = {'Product Name': product_names, 'Price': product_prices, 'Link':product_link}
    df = pd.DataFrame(data)
    df.to_csv('ebay_data.csv', index=False)
    print("CSV file 'ebay_data.csv' created successfully.")
    
    # Save data to JSON
    product_data = [{'Product Name': name, 'Price': price, 'Link': link} for name, price, link in zip(product_names, product_prices, product_link)]
    json_data = json.dumps(product_data, indent=4)
    with open('ebay_data.json', 'w') as json_file:
        json_file.write(json_data)
    print("JSON file 'ebay_data.json' created successfully.")
except Exception as e:
    print("An error occurred while saving the data:", e)
