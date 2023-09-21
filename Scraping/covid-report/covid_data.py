from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

url = "https://www.worldometers.info/coronavirus/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

data_table = soup.find('table', id="main_table_countries_today")
data = []

if data_table:
    rows = data_table.find_all('tr')
    for row in rows[2:]:
        cols = row.find_all('td')
        country_data = {
            'Country': cols[1].get_text(strip=True),
            'Total Cases': cols[2].get_text(strip=True),
            'Total Deaths': cols[4].get_text(strip=True),
            'Total Recovered': cols[6].get_text(strip=True),
            'Critical Cases': cols[8].get_text(strip=True),
            'Deaths/1M pop': cols[11].get_text(strip=True),
            'Tests/1M pop': cols[13].get_text(strip=True),
            'Population': cols[14].get_text(strip=True),
        }
        data.append(country_data)

df = pd.DataFrame(data)

df.to_csv('data.csv', index=False)
