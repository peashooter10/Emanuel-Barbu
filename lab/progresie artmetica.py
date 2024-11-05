lista_numere=[]
numar=int(input(""))
lista_numere.append(numar)
while numar!=-1:
    numar = int(input(""))
    lista_numere.append(numar)

lista_numere.pop()
contor=0
if(len(lista_numere))>=2:
    ratia=lista_numere[1]-lista_numere[0]
    print(ratia)
    for i in range(0, len(lista_numere)-1):
        ratie_noua=lista_numere[i+1]-lista_numere[i]
        if(ratie_noua==ratia):
            contor+=1
if contor==len(lista_numere)-1:
    print("Este progresie")