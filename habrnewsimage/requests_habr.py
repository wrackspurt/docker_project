import datetime
import json
import requests
from bs4 import BeautifulSoup


url = 'https://habr.com/ru/news/'
current = datetime.datetime.now()
creation_date = current.strftime("%d-%m-%y")
jpath = 'webimage/habrarticles.json'


def get_html_page(link):
    news_request = requests.get(link)
    news_content = news_request.text
    return news_content


def find_articles_data(html_page, type_data):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    data = parsed_page.find_all('a', class_='tm-article-snippet__title-link', href=True)
    result_list = list()
    if type_data == 'titles':
        for d in data:
            result_list.append(d.text)
    elif type_data == 'urls':
        for d in data:
            result_list.append('https://habr.com' + str(d['href']))
    return result_list


"""def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    headings = parsed_page.find_all('a', class_='tm-article-snippet__title-link')
    quantity = len(headings)
    title_list = list()
    for i in range(quantity):
        title_list.append(headings[i].text)
    return title_list"""


"""def find_links(html_page):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    urls = parsed_page.find_all('a', class_='tm-article-snippet__title-link', href=True)
    links_list = list()
    for i in urls:
        links_list.append('https://habr.com' + str(i['href']))
    return links_list"""


def publish_report(path, link, articles, links):
    articles_dict = []
    for i in range(len(articles)):
        articles_dict.append({"title": articles[i], "link": links[i]})
    titles = {
        "creation_date": creation_date,
        "url": link,
        "articles": articles_dict,
    }
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(titles, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    page = get_html_page(url)
    publish_report(jpath, url, find_articles_data(page, 'titles'), find_articles_data(page, 'urls'))
    with open(jpath, 'r', encoding='utf-8') as fl:
        all_data = json.load(fl)
    habr_titles = all_data['articles']
    for h in habr_titles:
        print(h['title'], ': ', h['link'])
    # print(find_articles(get_html_page(url)))
