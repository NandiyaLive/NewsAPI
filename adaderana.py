import requests
from bs4 import BeautifulSoup as bs


def findnews(category):
    newsDict = {"success": True, "category": category, "news": []}
    try:
        base_url = f"http://www.adaderana.lk/{category}/"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"
        }
        r = requests.get(base_url, headers=headers).text
        soup = bs(r, "lxml")
        stories = soup.findAll("div", class_="story-text")

        for story in stories:
            title = (
                story.find("h2", class_="visible-xs")
                .text.replace("\n", "")
                .replace("\x91", "")
                .replace("\x92", "")
            )
            url = story.find("a")["href"]
            imageUrl = story.find("img")["src"]
            content = story.find("p").text.replace(" MORE..", "")

            dateNtimespan = story.findAll("span")
            dateNtime = dateNtimespan[-1].text

            date = dateNtime.split("\xa0\xa0")[0].replace("| ", "")
            time = dateNtime.split("\xa0\xa0")[-1]

            newsOb = {
                "title": title,
                "url": url,
                "summary": content,
                "date": date,
                "time": time,
                "imageUrl": imageUrl,
            }

            newsDict["news"].append(newsOb)

        return newsDict

    except Exception:
        errorDict = {
            "success": False,
            "category": category,
            "error": "API Error. Please try again later.",
        }

        return errorDict
