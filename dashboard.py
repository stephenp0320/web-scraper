from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout
from datetime import datetime
import time

def create_dashboard(articles):
    table = Table(title="Payments Industry News Feed", 
                  title_style="bold magenta",
                  show_header=True,
                  header_style="bold cyan")
    
    table.add_column("Headline", style="yellow", width=50)
    table.add_column("Preview", style="white", width=60)
    
    for article in articles:
        table.add_row(
            article['title'][:50] + "..." if len(article['title']) > 50 else article['title'],
            article['desc'][:60] + "..." if len(article['desc']) > 60 else article['desc']
        )

    timestamp = Panel(
        f"[green]Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/green]",
        style="bold blue"
    )
    
    layout = Layout()
    layout.split_column(
        Layout(timestamp, size=3),
        Layout(table)
    )
    
    return layout
