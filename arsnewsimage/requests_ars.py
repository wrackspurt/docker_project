import datetime
import json
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://arstechnica.com/gadgets/'
current = datetime.datetime.now()
creation_date = current.strftime("%d-%m-%y")
jpath = '/storage/data/arsarticles.json'


def get_html_page(link):
    news_request = requests.get(link, verify=False)
    news_content = news_request.text
    return news_content


def find_articles_data(html_page, type_data):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    data = parsed_page.find_all('h2')
    result_list = list()
    if type_data == 'titles':
        for d in data:
            result_list.append(d.text)
    elif type_data == 'urls':
        for d in data:
            for i in d.find_all('a', href=True):
                result_list.append(i['href'])
    return result_list


def publish_report(path, link, articles, links):
    articles_dict = []
    # создание словарей, хранящих заголовки и ссылки
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
    while True:
        page = get_html_page(url)
        publish_report(jpath, url, find_articles_data(page, 'titles'), find_articles_data(page, 'urls'))
        # with open(jpath, 'r', encoding='utf-8') as fl:
        #    all_data = json.load(fl)
        # ars_titles = all_data['articles']
        # for a in ars_titles:
        #    print(a['title'], ': ', a['link'])
        # print(find_articles(get_html_page(url)))
