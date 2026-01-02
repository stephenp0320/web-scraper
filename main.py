from article_scraper import article_scraper
from dashboard import create_dashboard
import time
from rich.console import Console

console = Console()

def main():
    console.print("[bold green] Starting Payments News Monitor...[/bold green]\n")
    
    try:
        while True:
            articles = article_scraper()
            dashboard = create_dashboard(articles)
            
            console.clear()
            console.print(dashboard)
            console.print("\n[dim]Press Ctrl+C to stop | Updates every 60 seconds[/dim]")
            
            time.sleep(60)  
            
    except KeyboardInterrupt:
        console.print("\n[bold red] Monitor stopped[/bold red]")
if __name__ == ('__main__'):
     main()
