import requests
from bs4 import BeautifulSoup as bs


def web_scraper():
    url = 'https://www.paymentsdive.com/'
    responce = requests.get(url)
    soup = bs(responce.text, 'html.parser')
    
    selector = "#main-content > section"

    lines = soup.select_one(selector)

    res = lines.find_all("h3")
    res2 = lines.find_all("p")
    

    n = min(len(res), len(res2))
    for x in range(n):
        print("Heading --> " + str.strip(res[x].text))
        print("paragraph --> " + str.strip(res2[x].text))
        print("")


    with open("scraped_res.txt", "w") as f:
        for x, y in zip(res, res2):
            f.write(x.get_text(strip=True))
            f.write(y.get_text(strip=True))
    

if __name__ == ('__main__'):
    web_scraper()
