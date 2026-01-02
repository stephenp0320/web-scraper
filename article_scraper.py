import requests
from bs4 import BeautifulSoup as bs

def article_scraper(url, selector=None, headline_tag="h3"):
    try:
        res = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        soup = bs(res.text, 'html.parser')
        
        if selector:
            lines = soup.select_one(selector)
        else:
            lines = soup
        
        articles = []
        if lines:
            # Use the specified headline tag (h2, h3, etc.)
            headings = lines.find_all(headline_tag)
            
            for heading in headings[:10]:
                parent = heading.find_parent()
                description = parent.find("p") if parent else None
                link = heading.find("a") or (parent.find("a") if parent else None)
                
                # Skip if no actual text
                title = heading.text.strip()
                if not title or len(title) < 10:
                    continue
                
                articles.append({
                    "title": title,
                    "desc": description.text.strip() if description else "No description",
                    "link": link['href'] if link and link.get('href') else ""
                })
        
        print(f"Total articles collected from {url}: {len(articles)}")
        return articles
        
    except Exception as e:
        print(f"[ERROR] Failed to scrape {url}: {e}")
        return []