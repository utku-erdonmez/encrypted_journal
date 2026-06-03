from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def show_title():
    console.print(Panel("[bold cyan]Encrypted Journal[/bold cyan]"))

def show_message(msg, style="green"):
    console.print(f"[{style}]{msg}[/{style}]")

def ask_password():
    return Prompt.ask("Password", password=True)

def ask_input(prompt_text):
    return Prompt.ask(prompt_text)

def show_menu():
    console.print("\n[1] New Entry")
    console.print("[2] Timeline")
    console.print("[3] Random")
    console.print("[4] Search")
    console.print("[5] Exit")
    return Prompt.ask("Select")

def show_entry(entry):
    console.print(Panel(
        f"{entry['date']} {entry['time']}\n\n{entry['text']}",
        title="Journal Entry"
    ))

def print_list_item(i, e):
    preview = e["text"][:60].replace("\n", " ")
    console.print(f"[{i}] {e['date']} {e['time']} - {preview}")