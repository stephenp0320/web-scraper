import requests
from bs4 import BeautifulSoup as bs


def web_scraper():
    url = 'https://www.paymentsdive.com/'
    res = requests.get(url, timeout = 10)
    soup = bs(res.text, 'html.parser')
    
    selector = "#main-content > section"
    lines = soup.select_one(selector)

    articles = []
    for article in lines.find_all("article")[:10]:
        heading = article.find("h3")
        description = article.find("p")
        link = article.find("p")

        if heading:
            article.append({
                "title": heading.text.strip(),
                "desc": description.text.strip() if description else "No description",
                "link": link['href'] if link else ""
            })
    return articles



if __name__ == ('__main__'):
    web_scraper()
