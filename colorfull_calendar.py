import calendar
from rich.console import Console
from rich.table import Table

def display_colored_calendar(year):
    console = Console()
    months = [calendar.monthcalendar(year, m) for m in range(1, 13)]

    WEEK_DAYS_COLOR = "bold blue"
    month_name = calendar.month_name[month +1]
    # Create a table for the month
    table = Table(title= f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)
    
    # Add the days of the week as headers
    table.add_column("Sun", justify="center", style="bold red")
    table.add_column("Mon", justify="center", style=WEEK_DAYS_COLOR)
    table.add_column("Tue", justify="center", style=WEEK_DAYS_COLOR)
    table.add_column("Wed", justify="center", style=WEEK_DAYS_COLOR)
    table.add_column("Thu", justify="center", style=WEEK_DAYS_COLOR)
    table.add_column("Fri", justify="center", style=WEEK_DAYS_COLOR)
    table.add_column("Sat", justify="center", style="bold white")

    # Fill in the days of the month
    for week in months[month]:
        table.add_row(*[(str(day) if day != 0 else "") for day in week])    

    # Print the colored calendar
    console.print(table)
    console.print("\n")

if __name__ == "__main__":
    display_colored_calendar(2025)