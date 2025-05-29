import json
import random

bancnote = [[10,100], [5,100], [2,100], [1,100]] # [valoare, cantitate]
produse = [["lapte",7], ["paine",3], ["ciocolata",5], ["apa",2], ["cafea",9]] # [nume, pret]

lista_resturi = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
contor = 0
def min_coins(coins,total):
    dp = [float('inf')] * (total+1)
    dp[0] = 0

    for j in range(1,total + 1):
        for coin in coins:
            if coin <= j:
                dp[j] = min(dp[j],dp[j-coin]+1)

    return dp[total] if dp[total] != float('inf') else -1

def nema_rest(rest,produs,pret_produs,suma_platita):
    global contor
    print(f"Clientul cu nr. {contor} a cumparat: {produs} in valoarea de {pret_produs} lei.\nAcesta a platit {suma_platita} lei.")
    print(f"Nu se poate da restul in valoare de {rest}.")
    print(f"{rest} {produs} {pret_produs} {suma_platita} {lista_resturi[rest]}")

def gasire_combinatie(rest,produs,pret_produs,suma_platita):
    rest_platit = 0
    lista = []
    for i in range(len(bancnote)):
        if bancnote[i][1] == 0 and (rest_platit + bancnote[i][0] <= rest):
            nema_rest(rest,produs,pret_produs, suma_platita)
            return 0
        while bancnote[i][1] and (rest_platit + bancnote[i][0] <= rest):
            rest_platit = rest_platit + bancnote[i][0]
            bancnote[i][1] -= 1
            lista.append(bancnote[i][0])
        if rest_platit == rest:
            lista_resturi[rest] = lista
            return 1

def calculare_rest(suma_platita,produs):
    global contor
    pret_produs = 0
    for i in range(len(produse)):
        if produse[i][0] == produs:
            pret_produs = produse[i][1]
            continue
    if suma_platita - pret_produs >= 0:
        rest = suma_platita - pret_produs
    else:
        print("Fonduri insuficiente, săracule.")
        return 0
    if lista_resturi[rest]:
        print(
            f"Clientul cu nr. {contor} a cumparat: {produs} in valoarea de {pret_produs} lei.\nAcesta a platit {suma_platita} lei.\n"
            f"Restul oferit este {rest} lei care a fost platit cu urmatoarele bancnote {lista_resturi[rest]}.\n")
        for nr in lista_resturi[rest]:
            #print(nr)
            print(bancnote)
            if nr == 10 and (bancnote[0][1]>0):
                bancnote[0][1] = bancnote[0][1] - 1
                #print(f"bancnote de 10 ramase {bancnote[0][1]}")
            if nr == 5 and (bancnote[1][1]>0):
                bancnote[1][1] = bancnote[1][1] - 1
                #print(bancnote[1][1])
            if nr == 2 and (bancnote[2][1]>0):
                bancnote[2][1] = bancnote[2][1] - 1
                #print(bancnote[2][1])
            if nr == 1 and (bancnote[3][1]>0):
                bancnote[3][1] = bancnote[3][1] - 1
                #print(bancnote[3][1])
            if bancnote[0][1] == bancnote[1][1] == bancnote[2][1] == bancnote[3][1] == 0:
                return 0
    else:
        if gasire_combinatie(rest,produs,pret_produs,suma_platita) ==0:
            return 0
        print(f"Clientul cu nr. {contor} a cumparat: {produs} in valoarea de {pret_produs} lei.\nAcesta a platit {suma_platita} lei.\n"
              f"Restul oferit este {rest} lei care a fost platit cu urmatoarele bancnote {lista_resturi[rest]}.\n")

lista_clienti = [[] for j in range(1000)]
dictionar = {}
def generare_dictionar_clienti():
    global lista_clienti
    for i in range(1000):
        lista_clienti[i] = random.choice(produse)
    lista_produse = []
    lista_sume = []
    global dictionar
    keys = ["produse", "sume"]
    for i in range(1000):
        lista_produse.append(lista_clienti[i][0])
        lista_sume.append(lista_clienti[i][1]+random.randint(0,20))
    values = [lista_produse,lista_sume]
    for key, value in zip(keys,values):
        if key in dictionar:
            if isinstance(dictionar[key],list):
                dictionar[key].append(value)
            else:
                dictionar[key] = [dictionar[key],value]
        else:
            dictionar[key] = value

def rulare_calcul_rest():
    global contor
    l = list(zip(dictionar['produse'], dictionar['sume']))
    for pereche in l:
        contor = contor + 1
        if calculare_rest(pereche[1],pereche[0]) == 0:
            break

def main():
    global contor
    file = open('data.json','w', encoding= 'utf-8')
    generare_dictionar_clienti()
    json.dump(dictionar,file, indent = 4)
    rulare_calcul_rest()
main()
