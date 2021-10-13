from flask import Flask, render_template, redirect, url_for, request
import json


ARS_PATH = '/storage/data/arsarticles.json'
HABR_PATH = '/storage/data/habrarticles.json'

app = Flask(__name__)


def get_articles(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


ars_data = get_articles(ARS_PATH)
habr_data = get_articles(HABR_PATH)
# habr_titles = list()
# habr_links = list()
# тут лежат словари с заголовками и ссылками
habr_articles = habr_data['articles']
# for h in habr_data['articles']:
#    habr_titles.append(h['title'])
#    habr_links.append(h['link'])
# ars_titles = list()
# ars_links = list()
ars_articles = ars_data['articles']
# for a in ars_data['articles']:
#    ars_titles.append(a['title'])
#    ars_links.append(a['link'])


@app.route('/', methods=['GET', 'POST'])
def choose_source():
    sources = ["habr", "ars technica"]
    if request.method == 'POST':
        source = request.form.get('sources')
        if source == 'habr':
            return redirect(url_for('post_habr_articles'))
        elif source == 'ars technica':
            return redirect(url_for('post_ars_articles'))
    return render_template('dropdown.html', sources=sources)


@app.route('/habr_articles', methods=['GET', 'POST'])
def post_habr_articles():
    return render_template('habr_articles.html', date=habr_data['creation_date'], habr_url=habr_data['url'],
                           habr_articles=habr_articles)


@app.route('/ars_articles', methods=['GET', 'POST'])
def post_ars_articles():
    return render_template('ars_articles.html', date=ars_data['creation_date'], ars_url=ars_data['url'],
                           ars_articles=ars_articles)


@app.route('/back', methods=['POST'])
def back_to_start():
    return redirect(url_for('choose_source'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)


"""@app.route('/update_habr', methods=['POST'])
def update_habr_articles():
    return redirect(url_for('post_habr_articles'))"""


"""@app.route('/update_ars', methods=['POST'])
def update_ars_articles():
    return redirect(url_for('post_ars_articles'))"""


