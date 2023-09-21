import pandas as pd
import requests
from bs4 import BeautifulSoup

names = []
prices = []
desc = []
reviews = []

for i in range(2, 11):
    url = "https://www.flipkart.com/search?q=phones+under+50k&page=" + str(i)

    webdata = requests.get(url)
    soup = BeautifulSoup(webdata.content, "html.parser")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    name_elements = box.find_all("div", class_="_4rR01T")
    price_elements = box.find_all("div", class_="_30jeq3")
    desc_elements = box.find_all("ul", class_="_1xgFaf") 
    review_elements = box.find_all("div", class_="_3LWZlK")

    for i, name in enumerate(name_elements):
        names.append(name.text)

        if i < len(price_elements):
            prices.append(price_elements[i].text)
        else:
            prices.append("")

        if i < len(desc_elements):
            desc.append(desc_elements[i].text)
        else:
            desc.append("")

        if i < len(review_elements):
            reviews.append(review_elements[i].text)
        else:
            reviews.append("")

data = {
    "Product Name": names,
    "Price": prices,
    "Description": desc,
    "Reviews": reviews
}

df = pd.DataFrame(data)

df.to_csv("Flipkart_phones.csv", index=False)
