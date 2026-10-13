from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

def show_banner():
    banner_text = "[bold cyan]▲ ANTIGRAVITY ENGINE ▲[/bold cyan]\n[bold yellow]Autonomous Linux Zero-Bloat & FinOps Optimizer[/bold yellow]"
    console.print(Panel.fit(banner_text, border_style="cyan", box=box.DOUBLE))
    console.print("[dim]⚡ Defying System Gravity • Eliminating Server Bloat • Saving Cloud Costs[/dim]\n")

def display_scan_results(apt_mb, journal_str, docker_mb, zombies, high_mem, finops):
    table = Table(title="🛰️ System Deadweight & Telemetry Audit", box=box.ROUNDED)
    table.add_column("Audit Metric", style="cyan", no_wrap=True)
    table.add_column("Detected Bloat / Count", style="magenta")
    table.add_column("Gravity Impact", style="yellow")

    table.add_row("APT Package Cache", f"{apt_mb:.2f} MB", "Dead Storage Weight")
    table.add_row("System Logs (Journal)", f"{journal_str}", "Accumulated Log Pressure")
    table.add_row("Docker Cache / Images", f"{docker_mb:.2f} MB", "Reclaimable Container Bloat")
    table.add_row("Zombie Processes", f"{len(zombies)} detected", "CPU Leak" if zombies else "[green]Zero-G (Clean)[/green]")
    table.add_row("High-Memory Processes", f"{len(high_mem)} detected", "RAM Pressure" if high_mem else "[green]Optimal[/green]")

    console.print(table)
    console.print()

    fin_text = (
        f"[bold white]Estimated Monthly Cloud Waste:[/bold white] [bold red]${finops['monthly_waste_usd']} USD[/bold red]\n"
        f"[bold white]Potential Annual Infrastructure Savings:[/bold white] [bold green]${finops['annual_savings_usd']} USD / yr[/bold green]\n"
        f"[dim white]Calculated based on AWS EBS storage & cloud VM retention benchmarks.[/dim white]"
    )
    console.print(Panel(fin_text, title="💰 FinOps Economic Impact Report", border_style="yellow"))
