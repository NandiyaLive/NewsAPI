from flask import Flask, jsonify

from adaderana import findnews

app = Flask(__name__)


@app.route("/")
def home():
    homePage = {
        "Name": "Ada Derana News API",
        "Version": "1.0.0",
        "Description": "A simple API to fetch latest news from Ada Derana.",
        "Status": "Up",
        "Author": "Neranjana Prasad",
        "Web": "https://neranjana.me",
        "GitHub": "https://github.com/NandiyaLive/NewsAPI",
        "Usage": {
            "Hot News": "/hot-news",
            "Sports News": "/sports-news",
            "Entertainment News": "/entertainment-news",
            "Technology News": "/technology-news",
        },
    }
    return homePage


@app.route("/<query>")
def getNews(query):
    if query == "hot-news":
        return jsonify(findnews("hot-news"))
    elif query == "sports-news":
        return jsonify(findnews("sports-news"))
    elif query == "entertainment-news":
        return jsonify(findnews("entertainment-news"))
    elif query == "technology-news":
        return jsonify(findnews("technology-news"))
    else:
        return jsonify(
            {
                "success": False,
                "error": "Invalid category. Please use one of the following: hot-news, sports-news, entertainment-news, technology-news.",
            }
        )


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True)
