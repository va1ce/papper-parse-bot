import requests
import json
from bs4 import BeautifulSoup

#encoding="UTF-8"
headers ={"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36"}

def get_first_new():
    url = "https://www.pepper.ru/groups/laptop"

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "html5lib")
    articles_card = soup.find_all("article" , class_="thread")

    new_dict = {}

    for article in articles_card:
        article_title = article.find("img").get("alt")
        article_price = article.find("span" , class_="thread-price text--b cept-tp size--all-l size--fromW3-xl")
        if article_price is not None :
            article_price = article.find("span", class_="thread-price text--b cept-tp size--all-l size--fromW3-xl").text
        else:
            continue
        article_prices = article.find("span", class_="mute--text text--lineThrough size--all-l size--fromW3-xl cept-next-best-price")
        if article_prices is not None :
            article_prices = article.find("span", class_="mute--text text--lineThrough size--all-l size--fromW3-xl cept-next-best-price").text
        else:
            continue
        article_discount = article.find("span",class_="space--ml-1 size--all-l size--fromW3-xl cept-discount").text
        article_link = article.find("a").get("href")
        article_id = article_link.split("-")[-1]

        new_dict[article_id] = {
            "article_title": article_title,
            "article_price": article_price,
            "article_prices": article_prices,
            "article_discount": article_discount,
            "article_link": article_link
        }

    with open('new_dict.json', 'w', encoding="UTF-8") as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)


def chek_news_update():
    with open('new_dict.json', encoding="UTF-8") as file:
        new_dict = json.load(file)

    url = "https://www.pepper.ru/groups/laptop"

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "html5lib")
    articles_card = soup.find_all("article", class_="thread")
    fresh_new = {}
    for article in articles_card:
        article_link = article.find("a").get("href")
        article_id = article_link.split("-")[-1]


        if article_id in new_dict:
            continue
        else:
            article_title = article.find("img").get("alt")
            article_price = article.find("span", class_="thread-price text--b cept-tp size--all-l size--fromW3-xl")
            if article_price is not None:
                article_price = article.find("span",
                                             class_="thread-price text--b cept-tp size--all-l size--fromW3-xl").text
            else:
                continue
            article_prices = article.find("span",
                                          class_="mute--text text--lineThrough size--all-l size--fromW3-xl cept-next-best-price")
            if article_prices is not None:
                article_prices = article.find("span",
                                              class_="mute--text text--lineThrough size--all-l size--fromW3-xl cept-next-best-price").text
            else:
                continue
            article_discount = article.find("span", class_="space--ml-1 size--all-l size--fromW3-xl cept-discount").text
            new_dict[article_id] = {
                "article_title": article_title,
                "article_price": article_price,
                "article_prices": article_prices,
                "article_discount": article_discount,
                "article_link": article_link
            }
            fresh_new[article_id] = {
                "article_title": article_title,
                "article_price": article_price,
                "article_prices": article_prices,
                "article_discount": article_discount,
                "article_link": article_link
            }
    with open('new_dict.json', 'w', encoding="UTF-8") as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)

    return fresh_new


if __name__ == '__main__':
    #get_first_new()
    print(chek_news_update())


