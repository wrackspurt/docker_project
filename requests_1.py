import datetime
import json
import requests
from bs4 import BeautifulSoup


url = 'https://habr.com/ru/news/'
current = datetime.datetime.now()
creation_date = current.strftime("%d-%m-%y")
jpath = 'articles.json'


def get_html_page(link):
    news_request = requests.get(link)
    news_content = news_request.text
    return news_content


def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    headings = parsed_page.find_all('a', class_='tm-article-snippet__title-link')
    quantity = len(headings)
    title_list = list()
    for i in range(quantity):
        title_list.append(headings[i].text)
    return title_list


def publish_report(path, link, articles):
    articles_dict = []
    for i in range(len(articles)):
        articles_dict.append({"title": articles[i]})
    titles = {
        "creation_date": creation_date,
        "url": link,
        "articles": articles_dict,
    }
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(titles, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    publish_report(jpath, url, find_articles(get_html_page(url)))
