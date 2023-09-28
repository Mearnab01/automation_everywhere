import streamlit as st
from PIL import Image
import requests
import os

NEWS_API_KEY = os.environ["news_api"]
NEWS_API_URL = "https://newsapi.org/v2/everything?"
IMAGE_NOT_FOUND_URL = "URL_TO_DEFAULT_IMAGE"

st.set_page_config(page_title='Arth-News: Get news(By Arnab)📰 ')


def fetch_news_search_topic(topic):
    params = {
        "apiKey": NEWS_API_KEY,
        "q": topic
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    return data.get("articles", [])


def display_news(list_of_news, news_quantity):
    for index, news in enumerate(list_of_news[:news_quantity], 1):
        st.write(f'**({index}) {news["title"]}**')
        st.image(news.get("urlToImage", IMAGE_NOT_FOUND_URL), use_column_width=True)
        
        with st.expander(news["title"]):
            st.markdown(
                f'''<h6 style='text-align: justify;'>{news["description"]}"</h6>''',
                unsafe_allow_html=True)
            st.markdown(f"[Read more at {news['source']['name']}...]({news['url']})")
        
        st.success(f"Published Date: {news['publishedAt']}")


def run():
    st.title("Arth-News-Hub📰")
    image = Image.open('./Meta/newspaper_img.png')

    col1, col2, col3 = st.columns([3, 5, 3])

    with col1:
        st.write("")

    with col2:
        st.image(image, use_column_width=False)

    with col3:
        st.write("")

    user_topic = st.text_input("Enter your Topic🔍")
    no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)

    if st.button("Search") and user_topic != '':
        news_list = fetch_news_search_topic(user_topic)
        if news_list:
            st.subheader(f"✅ Here are some news articles for {user_topic.capitalize()}")
            display_news(news_list, no_of_news)
        else:
            st.error(f"No news articles found for {user_topic}")
    elif user_topic != '':
        st.warning("Please click the 'Search' button to fetch news articles.")

run()
