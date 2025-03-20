from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from bogosort import bogo_sort

# Root setup
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1600, 900)
root.config(bg='black')

# Variables
selected_alg = StringVar()
data = []
pause=False

def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        x0 = i * x_width
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=SW)
    root.update_idletasks()

def generate_color_array(length, color):
    return [color for _ in range(length)]

def generate_data():
    global data
    size = int(sizeEntry.get())
    min_val = 1
    max_val = size
    data = [random.randrange(min_val, max_val + 1) for _ in range(size)]
    draw_data(data, generate_color_array(len(data), 'red'))

def start_algorithm():
    global data
    if not data: return

    algorithm = algorithm_menu.get()
    if algorithm == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, draw_data, float(speed.get()))
    elif algorithm == 'Bubble Sort':
        bubble_sort(data, draw_data, float(speed.get()))
    elif algorithm == 'Merge Sort':
        merge_sort(data, draw_data, float(speed.get()))
    elif algorithm == 'Bogo Sort':
        bogo_sort(data, draw_data,float(speed.get()))

    draw_data(data, generate_color_array(len(data), 'green'))

def toggle_pause():
    global pause
    pause = not pause
    print("Script Paused" if pause else "Script Resumed")
    if not pause:
        run_script()
def run_script():
    global pause
    if not pause:
        start_algorithm()
        root.after(10, run_script)

UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algorithm_menu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Bogo Sort'])
algorithm_menu.grid(row=0, column=1, padx=5, pady=5, sticky=W)
algorithm_menu.current(0)

Label(UI_frame, text="Speed: ", bg='grey').grid(row=0, column=2, padx=5, pady=5, sticky=W)
speed = ttk.Combobox(UI_frame,values=['0.01', '0.25','0.5','1.0', '2.0'],width=10,state="readonly")
speed.grid(row=0, column=3, padx=5, pady=5, sticky=W)
speed.current(0)

Button(UI_frame, text="Start", command=start_algorithm, bg='orange').grid(row=0, column=4, padx=10, pady=5, sticky=W)

Label(UI_frame, text="Size: ", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry=ttk.Combobox(UI_frame,values=['8','16','32','64','128'],width=10,state="readonly")
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
sizeEntry.current(2)

Button(UI_frame, text="Generate", command=generate_data, bg='white').grid(row=1, column=2, padx=5, pady=5)
Button(UI_frame,text="Pause/Resume", command=toggle_pause,bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
