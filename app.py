from flask.helpers import url_for
from werkzeug.utils import redirect
import wikipedia
from flask import Flask, request, render_template, redirect

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
    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run()




