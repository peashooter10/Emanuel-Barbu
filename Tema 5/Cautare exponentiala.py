numar_iteratii = 0

def cautare_binara(lista,stanga,dreapta, val):
    global numar_iteratii
    st=stanga
    dr=dreapta
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

#cautare exponentiala
def cauta_pacient(tab,val):
    global numar_iteratii
    n=len(tab)
    if tab[0]==val:
        return(print(f"Dosarul pacientului cu numărul de identificare {val} a fost găsit la poziția 0 după {numar_iteratii} pași de căutare."))
    i=1
    while i<n and tab[i]<val:
        numar_iteratii+=1
        i*=2
    return cautare_binara(tab,i//2,min(i,n-1),val)


