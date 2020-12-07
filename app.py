from flask import Flask, jsonify
from adaderana import findnews

app = Flask(__name__)


@app.route('/')
def home():
    homePage = {
        "Name": "AdaDeranaNewsAPI",
        "Status": "Up",
        "Author": "Neranjana Prasad",
        "Web": "https://neranjana.tk"
    }
    return homePage


@app.route('/<query>')
def getNews(query):
    if query == "hot-news":
        return jsonify(findnews('hot-news'))
    elif query == "sports-news":
        return jsonify(findnews("sports-news"))
    elif query == "entertainment-news":
        return jsonify(findnews("entertainment-news"))
    elif query == "technology-news":
        return jsonify(findnews("technology-news"))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
