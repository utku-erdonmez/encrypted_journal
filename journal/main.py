from app.storage import load_data
from app.service import new_entry, get_random_entry, search_entries, get_entries
from app import ui

# --- MENÜ İŞLEMLERİ ---

def handle_new_entry(data, password):
    text = ui.ask_input("Write entry")
    new_entry(data, password, text)
    ui.show_message("Saved")

def handle_timeline(data, _):
    entries = get_entries(data)
    if not entries:
        return ui.show_message("No entries", "red")

    for i, e in enumerate(entries, 1):
        ui.print_list_item(i, e)

    sel = ui.ask_input("Select")
    if sel.isdigit() and 0 <= (index := int(sel) - 1) < len(entries):
        ui.show_entry(entries[index])

def handle_random(data, _):
    if e := get_random_entry(data):
        ui.show_entry(e)
    else:
        ui.show_message("No entries", "red")

def handle_search(data, _):
    results = search_entries(data, ui.ask_input("Search"))
    if not results:
        return ui.show_message("No results", "red")
        
    for i, e in enumerate(results, 1):
        ui.print_list_item(i, e)

# --- ANA UYGULAMA DÖNGÜSÜ ---

def main():
    ui.show_title()
    password = ui.ask_password()

    try:
        data = load_data(password)
    except Exception:
        return ui.show_message("Wrong password", "red")

    actions = {
        "1": handle_new_entry,
        "2": handle_timeline,
        "3": handle_random,
        "4": handle_search
    }

    while (choice := ui.show_menu()) != "5":
        action = actions.get(choice)
        if action:
            action(data, password) 
        else:
            ui.show_message("Invalid", "red")

if __name__ == "__main__":
    main()