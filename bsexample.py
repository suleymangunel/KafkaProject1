from bs4 import BeautifulSoup
import requests
import re
import lxml


def main():
    print("BS Example")
    rwp = requests.get("https://news.ycombinator.com/newest")
    soup = BeautifulSoup(rwp.content, 'html.parser')  # lxml can be use instead of html.parser
    # lstscript = soup.findAll(class_="athing")
    # for a in lstscript:
    #     id = a["id"]
    #     lnktmp = a.find_next(class_="titleline").find_next("a")
    #     if re.search("http", lnktmp["href"]) is not None:
    #         lnk = lnktmp["href"]
    #         score = a.find_next(class_="score").string.split()[0]
    #         desc = lnktmp.string
    #         print("Desc: "+str(desc) + " -> ID: " + str(id) + " -> Link: " + str(lnk) + " -> Score: " + str(score))

    article_ids = []
    article_texts = []
    article_links = []
    article_scores = []

    articles = soup.findAll(name="span", class_="titleline")
    scores = soup.findAll(name="span", class_="score")
    ids = soup.findAll(name="tr", class_="athing")

    for _id in ids:
        article_ids.append(str(_id["id"]))

    for article in articles:
        article_texts.append(article.getText())
        article_links.append(article.find_next(name="a")["href"])

    for score in scores:
        article_scores.append(int(score.getText().split()[0]))

    act = []
    for sn in range(len(article_ids)):
        tmp = {"id": article_ids[sn], "text": article_texts[sn], "link": article_links[sn], "score": article_scores[sn]}
        act.append(tmp)

    _result = list(x for x in act if x["score"] == max(article_scores))
    for _res in _result:
        print(_res["text"], " | Score: ", _res["score"])
