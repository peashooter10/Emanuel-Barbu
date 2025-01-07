#importăm biblioteca Tkinter pentru a-i putea accesa și folosi funcțiile
from tkinter import *
from tkinter import ttk
import random
import time

def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21 - bar11, 0)
    canvas.move(pos_1, bar12 - bar22, 0)

worker=None

def bubblesort():
    n = len(lengthlist)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lengthlist[j] > lengthlist[j + 1]:
                lengthlist[j], lengthlist[j + 1] = lengthlist[j + 1], lengthlist[j]
                barlist[j],barlist[j+1]=barlist[j+1],barlist[j]
                swap(barlist[j+1],barlist[j])
                yield

def bubble_sort():
    global worker
    worker = bubblesort()
    animate()

def mergesort(lengthlist, barlist):
    if len(lengthlist) > 1:
        mid = len(lengthlist) // 2
        left_half = lengthlist[:mid]
        right_half = lengthlist[mid:]
        bar_left = barlist[:mid]
        bar_right = barlist[mid:]

        # Recursively sort both halves
        yield from mergesort(left_half, bar_left)
        yield from mergesort(right_half, bar_right)

        i = j = k = 0

        # Merge process
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lengthlist[k] = left_half[i]
                barlist[k] = bar_left[i]
                swap(barlist[k], bar_left[i])  # Move bar visually
                i += 1
            else:
                lengthlist[k] = right_half[j]
                barlist[k] = bar_right[j]
                swap(barlist[k], bar_right[j])  # Move bar visually
                j += 1
            k += 1
            yield  # Yield after every visual update

        # Copy any remaining elements from the left half
        while i < len(left_half):
            lengthlist[k] = left_half[i]
            barlist[k] = bar_left[i]
            swap(barlist[k], bar_left[i])  # Move bar visually
            i += 1
            k += 1
            yield  # Yield after every visual update

        # Copy any remaining elements from the right half
        while j < len(right_half):
            lengthlist[k] = right_half[j]
            barlist[k] = bar_right[j]
            swap(barlist[k], bar_right[j])  # Move bar visually
            j += 1
            k += 1
            yield  # Yield after every visual update

def merge_sort():
    global worker
    worker = mergesort(lengthlist, barlist)
    animate()


def animate():
    global worker
    if worker is not None:
        try:
            next(worker)
            root.after(10, animate)
        except StopIteration:
            worker = None
        finally:
            root.after_cancel(animate)

#prin root creăm fereastra principală a aplicației
root = Tk()
root.title("Sorting algorithms visualized")

#prin mainframe creăm un grid în care vom pune elementele de care are nevoie aplicația
mainframe = ttk.Frame(root, padding="20 20 60 20")#stanga, sus, dreapta, jos
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#combobox pentru algoritmul de sortare utilizat
sortari = ["BubbleSort","MergeSort"]
selected_sortare = StringVar()

sortare_combobox = ttk.Combobox(mainframe, textvariable=selected_sortare, values=sortari)
sortare_combobox.grid(column=0, row=1, pady=10)
sortare_combobox.set("Alege un algoritm")
ttk.Label(mainframe, text="Algoritm:").grid(column=0, row=0, sticky=W)

#combobox pentru numarul de elemente
elemente=["32","64","128","256"]
selected_element=StringVar()

element_combobox = ttk.Combobox(mainframe, textvariable=selected_element, values=elemente)
element_combobox.grid(column=0, row=3, pady=10)
element_combobox.set("Nr. de elemente")
ttk.Label(mainframe, text="Nr. Elemente:").grid(column=0, row=2, sticky=W)

#crearea canvas-ului
inaltime_canvas=300
latime_canvas=800
canvas = Canvas(root, width=latime_canvas, height=inaltime_canvas, background='black')
canvas.grid(column=0, row=2, sticky=(N, W, E, S))

barlist=[]
lengthlist = []

def generare():
    global barlist, lengthlist
    canvas.delete("all")
    barlist.clear()
    lengthlist.clear()

    nbar=int(selected_element.get()) if selected_element.get().isdigit() else 32
    lat=canvas.winfo_width()//nbar

    for i in range(nbar):
        inalt=random.randint(10,290)

        x1 = i * lat
        y1 = inaltime_canvas
        x2 = (i + 1) * lat
        y2 = inaltime_canvas - inalt
        bar = canvas.create_rectangle(x1, y1, x2, y2, fill="white")

        barlist.append(bar)
        lengthlist.append(inalt)

        minim=300
        maxim=0

        for i in range(0,len(lengthlist)):
            if lengthlist[i] > maxim:
                maxim=lengthlist[i]
        for i in range(0,len(lengthlist)):
            if lengthlist[i]<minim:
                minim=lengthlist[i]

        for i in range(0,len(lengthlist)):
            if lengthlist[i] == minim:
                canvas.itemconfig(barlist[i], fill='red')
            if lengthlist[i] == maxim:
                canvas.itemconfig(barlist[i], fill='green')
            if lengthlist[i]!=minim and lengthlist[i]!=maxim:
                canvas.itemconfig(barlist[i], fill='white')



def start():
    alegere=selected_sortare.get()
    if alegere=="BubbleSort":
        bubble_sort()
    if alegere=="MergeSort":
        merge_sort()



ttk.Button(mainframe, text="generare", command=generare).grid(column=0, row=4, pady=10)
ttk.Button(mainframe, text="Start Sorting", command=start).grid(column=0, row=5, pady=10)

root.mainloop()