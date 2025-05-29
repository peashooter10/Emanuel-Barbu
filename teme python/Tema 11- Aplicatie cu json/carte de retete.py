import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "recipes.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

window = tk.Tk()
window.title("Aplicatie")
window.geometry("500x650")

#nume rețetă
tk.Label(window, text="Numele retetei:").pack(anchor='w', padx=10, pady=(10, 0))
recipe_name_entry = tk.Entry(window, width=50)
recipe_name_entry.pack(padx=10, pady=5)

#ingrediente
tk.Label(window, text="Ingrediente:").pack(anchor='w', padx=10, pady=(10, 0))
ingredients_text = tk.Text(window, height=10, width=60)
ingredients_text.pack(padx=10, pady=5)

#instructiuni
tk.Label(window, text="Instructiuni:").pack(anchor='w', padx=10, pady=(10, 0))
instructions_text = tk.Text(window, height=10, width=60)
instructions_text.pack(padx=10, pady=5)

#dropdown menu
tk.Label(window, text="Incarcare:").pack(anchor='w', padx=10, pady=(15, 0))
dropdown_var = tk.StringVar()
dropdown_menu = tk.OptionMenu(window, dropdown_var, "")
dropdown_menu.pack(padx=10, pady=5)

def refresh_dropdown():
    recipes = load_data()
    menu = dropdown_menu["menu"]
    menu.delete(0, "end")
    if recipes:
        for name in recipes.keys():
            menu.add_command(label=name, command=lambda v=name: dropdown_var.set(v))
        dropdown_var.set("Alege o retea")
    else:
        dropdown_var.set("Nu exista retete")

def get_next_id(recipes):
    max_id = 0
    for detalii in recipes.values():
        if "id" in detalii and isinstance(detalii["id"], int):
            max_id = max(max_id, detalii["id"])
    return max_id + 1

def save_recipe():
    name = recipe_name_entry.get().strip()
    ingredients = ingredients_text.get("1.0", tk.END).strip()
    instructions = instructions_text.get("1.0", tk.END).strip()

    if not name:
        messagebox.showerror("Eroare", "Numele retetei nu poate fi gol.")
        return

    recipes = load_data()

    #dacă rețeta există deja se păstrează id-ul
    if name in recipes:
        current_id = recipes[name].get("id", get_next_id(recipes))
    else:
        current_id = get_next_id(recipes)

    recipes[name] = {
        "ingredients": ingredients,
        "instructions": instructions,
        "id": current_id
    }

    save_data(recipes)
    refresh_dropdown()
    messagebox.showinfo("Salvat", f"Reteta '{name}' a fost salvata")
def load_selected_recipe():
    name = dropdown_var.get()
    recipes = load_data()
    if name in recipes:
        recipe = recipes[name]
        recipe_name_entry.delete(0, tk.END)
        recipe_name_entry.insert(0, name)

        ingredients_text.delete("1.0", tk.END)
        ingredients_text.insert("1.0", recipe["ingredients"])

        instructions_text.delete("1.0", tk.END)
        instructions_text.insert("1.0", recipe["instructions"])

        print(f"ID pentru '{name}': {recipe.get('id', 'No ID')}")
def clear_recipe():
    recipe_name_entry.delete(0, tk.END)
    ingredients_text.delete("1.0", tk.END)
    instructions_text.delete("1.0", tk.END)
def delete_recipe():
    name = dropdown_var.get()
    if not name or name in ["Alege o reteta", "Nu exista retete"]:
        messagebox.showerror("Eroare", "Alege o reteta valida,")
        return

    recipes = load_data()
    if name in recipes:
        confirm = messagebox.askyesno("Confirma", f"Esti sigur ca vrei sa stergi'{name}'?")
        if confirm:
            del recipes[name]
            save_data(recipes)
            refresh_dropdown()
            clear_recipe()
            messagebox.showinfo("Stergere", f"Reteta'{name}'a fost stearsa")

# Butoane
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

save_button = tk.Button(button_frame, text="Salvare", command=save_recipe)
save_button.grid(row=0, column=0, padx=10)

load_button = tk.Button(button_frame, text="Incarcare", command=load_selected_recipe)
load_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(button_frame, text="Golire", command=clear_recipe)
clear_button.grid(row=0, column=2, padx=10)

delete_button = tk.Button(button_frame, text="Stergere", command=delete_recipe)
delete_button.grid(row=0, column=3, padx=10)

refresh_dropdown()
window.mainloop()
