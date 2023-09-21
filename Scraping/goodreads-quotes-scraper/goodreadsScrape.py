import requests
from bs4 import BeautifulSoup

def get_books_by_genre(term):
    url = f'https://www.goodreads.com/genres/new_releases/{term}'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        big_box_body = soup.find('div', class_='bigBoxBody')
        
        if big_box_body is not None:
            cover_rows = big_box_body.find_all('div', class_='coverRow')

            for cover_row in cover_rows:
                a_tags = cover_row.find_all('a')

                for a_tag in a_tags:
                    href = a_tag.get('href')
                    print(f'Links: https://www.goodreads.com{href}', "\n")
        else:
            print(f'No books found for genre: {term}')

    else:
        print(f'Failed to retrieve the web page for genre: {term}. Status code:', response.status_code)

user_input = input("Which type of book do you want to read (fiction/biography/...): ")
get_books_by_genre(user_input)
