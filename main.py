from article_scraper import article_scraper
from dashboard import create_dashboard
import time
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

sources = {
    "1": {
        "name": "Payments Dive", 
        "url": "https://www.paymentsdive.com/",
        "selector": "#main-content > section",
        "headline_tag": "h3" 
    },
    "2": {
        "name": "Independent", 
        "url": "https://www.independent.ie/",
        "selector": None,  
        "headline_tag": "h3" 
    },
    "3": {
        "name": "Bloomberg", 
        "url": "https://www.bloomberg.com/europe",
        "selector": None,
        "headline_tag": "h2",
        "note": "⚠️ Has bot detection - may not work"
    },
    "4": {
        "name": "F1", 
        "url": "https://www.formula1.com/",
        "selector": None,
        "headline_tag": "h2"  
    },
    "5": {
        "name": "Hacker News", 
        "url": "https://news.ycombinator.com/",
        "selector": ".itemlist",
        "headline_tag": "span",  
        "note": "Uses different structure"
    },
}



def choose_sources():
    console.print(Panel("[bold cyan]📰 Available News Sources[/bold cyan]", style="blue"))
    
    for key, src in sources.items():
        console.print(f"  {key}. {src['name']}")
    
    console.print("\n[yellow]Enter numbers separated by commas (e.g., 1,3,4) or 'all' for everything:[/yellow]")
    choice = Prompt.ask("Your choice")
    
    if choice.lower() == 'all':
        return list(sources.values())
    
    selected = []
    for num in choice.split(','):
        num = num.strip()
        if num in sources:
            selected.append(sources[num])
    
    return selected

def main():
    selected_sources = choose_sources()
    
    console.print(f"\n[bold green] Monitoring {len(selected_sources)} source(s)...[/bold green]\n")
    try:
        while True:
            all_articles = []
            for source in selected_sources:
                try: 
                    articles = article_scraper(
                        source['url'], 
                        source.get('selector'),
                        source.get('headline_tag', 'h3')
                    )
                    for article in articles:
                        article['source'] = source['name']
                    all_articles.extend(articles)
                except Exception as e:
                    console.print(f"[red]Error scraping {source['name']}: {e}[/red]")
            
        
            dashboard = create_dashboard(all_articles)
            console.clear()
            console.print(dashboard)
            console.print("\n[dim]Press Ctrl+C to stop | Updates every 60 seconds[/dim]")
            time.sleep(60)
            
    except KeyboardInterrupt:
        console.print("\n[bold red] Monitor stopped[/bold red]")

if __name__ == ('__main__'):
     main()
