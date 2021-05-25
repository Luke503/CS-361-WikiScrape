from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.wrappers import Response
import wikipedia
import requests
from flask import *

app = Flask(__name__)

@app.route('/')
def search_input():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def search_result():
    text = request.form['text']
    search = wikipedia.search(text)
    first_article = search[0]
    summary = wikipedia.summary(first_article, sentences=10)
    result = summary
    url = (f'https://translator-osu.herokuapp.com/translate-to?text={summary}&language=French')
    response = requests.get(url)
    return render_template("index.html", result=result, response=response.text)


@app.route('/scrape', methods=['POST', 'GET'])
def scrape_info():
    take = request.args.get('take')
    search = wikipedia.search(take)
    first_article = search[0]
    summary = wikipedia.summary(first_article, sentences=10)
    return (summary)




if __name__ == '__main__':
    app.run()



