from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    
movie_name=[]
movie_link=[]
movie_rating = []   
movie_duration=[]
movie_genre=[]
movie_director=[]

def fetch_data(soup):
    try:
        box=soup.find("div",class_="lister-list")

        #name
        titles=box.find_all("h3",class_="lister-item-header")
        for title in titles:
            movie_sentence_title=title.text.split()
            movie_name.append(' '.join(movie_sentence_title[1:]))
        
        #link
        links=box.find_all("div",class_="lister-item-image")
        for link in links:
            movie_link.append(f"https://www.imdb.com/{link.a['href']}")

        #rating
        ratings=box.find_all("strong")
        for rating in ratings:
            movie_rating.append(rating.text.strip())

        #duration
        durations=box.find_all("span",class_="runtime")
        for duration in durations:
            movie_duration.append(duration.text.strip())
        
        #genre
        genres=box.find_all("span",class_="genre")
        for genre in genres:
            movie_genre.append(genre.text.strip())

        #director
        directors=box.find_all("p",class_="")
        for director in directors:
            movie_director.append(director.a.text)

    except AttributeError as e:
            print(e)

if __name__ == "__main__":
    for i in range(1,1000,100):
        url=f"https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating&start={i}"
        soup=get_data(url)
        if soup:
            fetch_data(soup)

data = {
        'Name': movie_name,
        'Link': movie_link,
        'Rating': movie_rating,
        'Duration': movie_duration,
        'Genre': movie_genre,
        'Director': movie_director
    }
df = pd.DataFrame(data)
df.to_csv("movie.csv",index=False)
