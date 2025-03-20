#Să se creeze o funcție care să primească parametrii datele de naștere ale unor persoane. Se va adăuga, pentru fiecare persoană, anul nașterii, luna nașterii și ziua nașterii. Fiecare persoană a căror date sunt adăugate în funcție primește un număr de ordine de la 1 la n, unde n este numărul de persoane adăugate. Să se determine numărul de ordine al celei mai tinere și al celei mai în vârstă persoană dintre cele date.
#Funcția afișează pe prima linie a ecranului numărul de ordine al celei mai tinere persoane, iar pe a doua linie numărul de ordine al celei mai în vârstă persoane
def sortare(l,k):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j][k]>l[j+1][k]:
                l[j][k],l[j+1][k]=l[j+1][k],l[j][k]

def p_1013(l):
    for i in range(3):
        sortare(l,i)
    print(l)

p_1013([
    [2003, 12, 17],
    [2011, 1, 12],
    [2003, 12, 19],
    [2011, 6, 29],
    [2011, 6, 30]
])

