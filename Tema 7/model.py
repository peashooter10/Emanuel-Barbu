from tkinter import *
from tkinter import ttk
import random

# Create the main application window
root = Tk()
root.title("Sorting Algorithms Visualized")

# Create a grid frame for layout
mainframe = ttk.Frame(root, padding="20 20 60 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Combobox for selecting the sorting algorithm
sortari = ["BubbleSort", "SelectionSort", "BogoSort"]
selected_sortare = StringVar()
sortare_combobox = ttk.Combobox(mainframe, textvariable=selected_sortare, values=sortari)
sortare_combobox.grid(column=0, row=1, pady=10)
sortare_combobox.set("Alege un algoritm")
ttk.Label(mainframe, text="Algoritm:").grid(column=0, row=0, sticky=W)

# Combobox for selecting the number of elements
elemente = ["32", "64", "128"]
selected_element = StringVar()
element_combobox = ttk.Combobox(mainframe, textvariable=selected_element, values=elemente)
element_combobox.grid(column=0, row=3, pady=10)
element_combobox.set("Nr. de elemente")
ttk.Label(mainframe, text="Nr. Elemente:").grid(column=0, row=2, sticky=W)

# Create a canvas for visualization
latime_canvas=600
inaltime_canvas=300
canvas = Canvas(root, width=latime_canvas, height=inaltime_canvas, background='black')
canvas.grid(column=0, row=2, sticky=(N, W, E, S))

# List to hold bar objects and their lengths
barlist = []
lengthlist = []


def generate_bars():
    """Generate bars dynamically based on the selected number of elements."""
    global barlist, lengthlist
    canvas.delete("all")
    barlist.clear()
    lengthlist.clear()

    num_bars = int(selected_element.get()) if selected_element.get().isdigit() else 10
    bar_width = canvas.winfo_width() // num_bars

    for i in range(num_bars):
        height = random.randint(10, 190)
        bar = canvas.create_rectangle(
            i * bar_width, inaltime_canvas, (i + 1) * bar_width, inaltime_canvas - height, fill='white'
        )
        barlist.append(bar)
        lengthlist.append(height)


def start_sorting():
    """Placeholder function for starting the sorting process."""
    selected = selected_sortare.get()
    if selected == "BubbleSort":
        bubble_sort()
    elif selected == "BogoSort":
        print("BogoSort is impractical to visualize here!")
    else:
        print("Select a sorting algorithm!")


def bubble_sort():
    """Perform a simple Bubble Sort and update the canvas."""
    n = len(lengthlist)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lengthlist[j] > lengthlist[j + 1]:
                # Swap lengths
                lengthlist[j], lengthlist[j + 1] = lengthlist[j + 1], lengthlist[j]

                # Redraw bars
                canvas.coords(barlist[j], j * 10, 200, (j + 1) * 10, 200 - lengthlist[j])
                canvas.coords(barlist[j + 1], (j + 1) * 10, 200, (j + 2) * 10, 200 - lengthlist[j + 1])
                root.update_idletasks()


# Buttons
ttk.Button(mainframe, text="Generate Bars", command=generate_bars).grid(column=0, row=4, pady=10)
ttk.Button(mainframe, text="Start Sorting", command=start_sorting).grid(column=0, row=5, pady=10)

# Run the application
root.mainloop()
