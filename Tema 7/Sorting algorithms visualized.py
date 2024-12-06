#importăm biblioteca Tkinter pentru a-i putea accesa și folosi funcțiile
from tkinter import *
from tkinter import ttk
import random

#prin root creăm fereastra principală a aplicației
root = Tk()
root.title("Sorting algorithms visualized")

#prin mainframe creăm un grid în care vom pune elementele de care are nevoie aplicația
mainframe = ttk.Frame(root, padding="20 20 60 20")#stanga, sus, dreapta, jos
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#combobox pentru algoritmul de sortare utilizat
sortari = ["BubbleSort", "SelectionSort", "BogoSort"]
selected_sortare = StringVar()

sortare_combobox = ttk.Combobox(mainframe, textvariable=selected_sortare, values=sortari)
sortare_combobox.grid(column=0, row=1, pady=10)
sortare_combobox.set("Alege un algoritm")
ttk.Label(mainframe, text="Algoritm:").grid(column=0, row=0, sticky=W)

#combobox pentru numarul de elemente
elemente=["10", "20", "30"]
selected_element=StringVar()

element_combobox = ttk.Combobox(mainframe, textvariable=selected_element, values=elemente)
element_combobox.grid(column=0, row=3, pady=10)
element_combobox.set("Nr. de elemente")
ttk.Label(mainframe, text="Nr. Elemente:").grid(column=0, row=2, sticky=W)

#button = ttk.Button(root, text='Shuffle', command=submitForm)

#crearea canvas-ului
canvas = Canvas(root, width=400, height=200, background='black')
canvas.grid(column=0, row=2, sticky=(N, W, E, S))

#crearea unei linii
#canvas.create_rectangle(3,200,13,100 , fill='white')
#crearea mai multor linii

barlist=[]
lengthlist = []
nbar=0

def generare():
    global barlist, lengthlist
    canvas.delete("all")
    barlist.clear()
    lengthlist.clear()
    nbar=int(selected_element.get())


for i in range(nbar):
    inbar=canvas.winfo_height()//nbar
    latbar=canvas.winfo_width()//nbar
    x1=i*latbar
    y1=(i+1)*inbar
    x2=(i+1)*latbar
    y2=i*inbar
    bar=canvas.create_rectangle(x1,y1,x2,y2,fill="white")
    barlist.append(bar)
    lengthlist.append(inbar)

for bar in barlist:
    bar = canvas.coords(bar)
    length = bar[1] - bar[0]
    lengthlist.append(length)



root.mainloop()