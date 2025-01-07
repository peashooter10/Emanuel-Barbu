from tkinter import *
from tkinter import ttk
import random

def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21 - bar11, 0)
    canvas.move(pos_1, bar12 - bar22, 0)

worker = None

def bubblesort():
    n = len(lengthlist)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lengthlist[j] > lengthlist[j + 1]:
                lengthlist[j], lengthlist[j + 1] = lengthlist[j + 1], lengthlist[j]
                barlist[j], barlist[j + 1] = barlist[j + 1], barlist[j]
                swap(barlist[j], barlist[j + 1])
                yield

def merge_sort_worker(low, high):
    if low < high:
        mid = (low + high) // 2
        yield from merge_sort_worker(low, mid)
        yield from merge_sort_worker(mid + 1, high)
        yield from merge(low, mid, high)

def merge(low, mid, high):
    left = lengthlist[low:mid + 1]
    right = lengthlist[mid + 1:high + 1]
    left_bars = barlist[low:mid + 1]
    right_bars = barlist[mid + 1:high + 1]

    i = j = 0
    for k in range(low, high + 1):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            lengthlist[k] = left[i]
            barlist[k] = left_bars[i]
            swap(barlist[k], barlist[low + i])
            i += 1
        else:
            lengthlist[k] = right[j]
            barlist[k] = right_bars[j]
            swap(barlist[k], barlist[mid + 1 + j])
            j += 1
        yield

def merge_sort():
    global worker
    worker = merge_sort_worker(0, len(lengthlist) - 1)
    animate()

def animate():
    global worker
    if worker is not None:
        try:
            next(worker)
            root.after(10, animate)
        except StopIteration:
            worker = None

# Main application setup
root = Tk()
root.title("Sorting Algorithms Visualized")

mainframe = ttk.Frame(root, padding="20 20 60 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sortari = ["BubbleSort", "MergeSort"]
selected_sortare = StringVar()

sortare_combobox = ttk.Combobox(mainframe, textvariable=selected_sortare, values=sortari)
sortare_combobox.grid(column=0, row=1, pady=10)
sortare_combobox.set("Alege un algoritm")
ttk.Label(mainframe, text="Algoritm:").grid(column=0, row=0, sticky=W)

elemente = ["32", "64", "128", "256"]
selected_element = StringVar()

element_combobox = ttk.Combobox(mainframe, textvariable=selected_element, values=elemente)
element_combobox.grid(column=0, row=3, pady=10)
element_combobox.set("Nr. de elemente")
ttk.Label(mainframe, text="Nr. Elemente:").grid(column=0, row=2, sticky=W)

canvas = Canvas(root, width=800, height=300, background='black')
canvas.grid(column=0, row=2, sticky=(N, W, E, S))

barlist = []
lengthlist = []

def generare():
    global barlist, lengthlist
    canvas.delete("all")
    barlist.clear()
    lengthlist.clear()

    nbar = int(selected_element.get()) if selected_element.get().isdigit() else 32
    lat = canvas.winfo_width() // nbar

    for i in range(nbar):
        inalt = random.randint(10, 290)
        x1 = i * lat
        y1 = 300
        x2 = (i + 1) * lat
        y2 = 300 - inalt
        bar = canvas.create_rectangle(x1, y1, x2, y2, fill="white")

        barlist.append(bar)
        lengthlist.append(inalt)

    minim = min(lengthlist)
    maxim = max(lengthlist)

    for i in range(len(lengthlist)):
        if lengthlist[i] == minim:
            canvas.itemconfig(barlist[i], fill='red')
        elif lengthlist[i] == maxim:
            canvas.itemconfig(barlist[i], fill='green')
        else:
            canvas.itemconfig(barlist[i], fill='white')

def start():
    alegere = selected_sortare.get()
    if alegere == "BubbleSort":
        worker = bubblesort()
        animate()
    elif alegere == "MergeSort":
        merge_sort()

ttk.Button(mainframe, text="Generare", command=generare).grid(column=0, row=4, pady=10)
ttk.Button(mainframe, text="Start Sorting", command=start).grid(column=0, row=5, pady=10)

root.mainloop()
