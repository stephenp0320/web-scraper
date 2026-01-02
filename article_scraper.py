import requests
from bs4 import BeautifulSoup as bs

def article_scraper():
    url = 'https://www.paymentsdive.com/'
    res = requests.get(url, timeout=10)
    soup = bs(res.text, 'html.parser')
    
    selector = "#main-content > section"
    lines = soup.select_one(selector)
    
    
    articles = []
    if lines:
        headings = lines.find_all("h3")
        
        for heading in headings[:10]:
            parent = heading.find_parent()
            description = parent.find("p") if parent else None
            link = heading.find("a") or (parent.find("a") if parent else None)
            
            articles.append({
                "title": heading.text.strip(),
                "desc": description.text.strip() if description else "No description",
                "link": link['href'] if link and link.get('href') else ""
            })
    
    print(f"Total articles collected: {len(articles)}")
    return articles