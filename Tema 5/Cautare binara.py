numar_iteratii = 0

def cauta_pacient(lista, val):
    global numar_iteratii
    st=0
    dr=len(lista)-1
    mijloc=(st+dr)//2
    while st<=dr:
        if val==lista[mijloc]:
            return(print(f"Dosarul pacientului cu numărul de identificare {val} a fost găsit la poziția {mijloc} după {numar_iteratii} pași de căutare."))
        if val<lista[mijloc]:
            dr=mijloc-1
        if val>lista[mijloc]:
            st=mijloc+1
        numar_iteratii+=1
        mijloc=(st+dr)//2
    return(print(f"Dosarul pacientului cu numărul de identificare {val} nu a fost găsit. Total pași efectuați: {numar_iteratii}."))









