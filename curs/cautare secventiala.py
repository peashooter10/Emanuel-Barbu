tab=[1,2,4,7,9,11,13,17,21,24]

def cautare_secventiala(tab,val):
    n=len(tab)
    for i in range(n):
        if tab[i]==val:
            return i
    return -1

numar=int(input(""))
a=cautare_secventiala(tab,numar)
print(a)