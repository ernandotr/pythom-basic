from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
console.clear()
table = Table(title="Top languages")
table.add_column("Language", justify="left", style="cyan")
table.add_column("Score", justify="left", style="magenta")
table.add_row("Python", "10/10")
table.add_row("JavaScript", "9/10")
table.add_row("C++", "8/10")
table.add_row("Java", "10/10")
console.print(Panel("[bold cyan]Programming Languages[/bold cyan]", style="green"))
console.print(Panel(table, border_style="yellow"))