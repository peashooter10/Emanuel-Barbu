import random
from sorting_algorithms_visualized import canvas, barlist, lengthlist, root

def redraw(list,i,j):
    canvas.coords(barlist[j], j * 10, 200, (j + 1) * 10, 200 - lengthlist[j])
    canvas.coords(barlist[j + 1], (j + 1) * 10, 200, (j + 2) * 10, 200 - lengthlist[j + 1])
    root.update_idletasks()

#bubblesort
def bubblesort(list):
    n=len(list)
    ok=False
    while ok==False:
        c=0
        for i in range (0,len(list)-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                redraw(list,i,i+1)
            else:
                c+=1
        if c==len(list):
            ok=True
""""
#bogosort
def bogoSort(list):
    n = len(list)
    while (is_sorted(list) == False):
        shuffle(list)
def is_sorted(list):
    n = len(list)
    for i in range(0, n - 1):
        if (list[i] > list[i + 1]):
            return False
    return True
def shuffle(list):
    n = len(list)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        list[i], list[r] = list[r], list[i]
        redraw(list,i,r)
""""
#selectionsort
def selectionsort(list):
    for i in range(0,len(list)):
        for j in range(i,len(list)-1):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
                redraw(list,i,j)
#mergesort
def mergesort(lista):
    if len(lista)>1:
        mijl=len(lista)//2
        st=lista[:mijl]
        dr=lista[mijl:]
        mergesort(st)
        mergesort(dr)
    i,j,k=0,0,0
    while i<len(st) and j<len(dr):
        if st[i]<dr[i]:
            lista[k]=st[i]
            i+=1
        else:
            lista=dr[j]
            j+=1
        k+=1
    while i<len(st):
        list[k]=st[i]
        i+=1
        k+=1
    while j<len(dr):
        list[k]=dr[j]
        j+=1
        k+=1
    #redraw(list,i,j)
