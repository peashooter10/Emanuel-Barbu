import json
import random

from numpy.random import randint


def citeste_date(FILENAME):
    #citesc din fisier si returnez fisierul json ca și un dicționar în python
    with open(FILENAME, 'r') as f:
        return json.load(f)

def calculeaza_rest(bancnote_disponibile, rest):
    # lista care va conține numărul de bancnote folosite:[0,0,0,0,0] și fac un vector de frecvență
    combinatie = [0] * len(bancnote_disponibile)

    # indexi_sortati este lista in care vom pune bancnotele disponibile
    indexi_sortati = list(range(len(bancnote_disponibile)))

    # sortez indexi descrecator pentru a-i putea parcurge în bucla for
    for i in range(len(indexi_sortati)):
        for j in range(len(indexi_sortati) - 1 - i):
            if bancnote_disponibile[indexi_sortati[j]]['valoare'] < bancnote_disponibile[indexi_sortati[j + 1]][
                'valoare']:
                indexi_sortati[j], indexi_sortati[j + 1] = indexi_sortati[j + 1], indexi_sortati[j]

    # în for parcurg indexi în ordine descrescătoare, dacă mai există bancnote în stoc le folosesc,
    # iar dacă nu continui în for cu o bancnotă de valoare mai mică
    for i in indexi_sortati:
        valoare = bancnote_disponibile[i]['valoare']
        stoc = bancnote_disponibile[i]['stoc']
        nr_bancnote = min(rest // valoare, stoc)
        combinatie[i] = nr_bancnote
        rest -= nr_bancnote * valoare

    # dacă restul este egal cu 0 atunci din stoc scad combinația pentru a actualiza stocul și trimit
    # stocul actualizat și combinația de bancnote folosită pentru a da restul
    if rest == 0:
        for i in range(len(bancnote_disponibile)):
            bancnote_disponibile[i]['stoc'] -= combinatie[i]
        return bancnote_disponibile, combinatie
    else:
        return 0, 0

def afiseaza_rest(bancnote_disponibile, combinatie):
    # afisez restul
    valori = [b['valoare'] for b in bancnote_disponibile]
    for i in range(len(combinatie)):
        if combinatie[i] > 0:
            print(f"{combinatie[i]}x{valori[i]} lei")

def genereaza_bancnote_client(valori_bancnote, pret):
    # generez bancnotele folosite de către client
    while True:
        bancnote_client = random.choices(valori_bancnote, k=random.randint(1, 5))
        suma = sum(bancnote_client)
        if pret <= suma <= pret + 20:
            return bancnote_client, suma
def adauga_bancnote_in_stoc(bancnote_disponibile, bancnote_client):
    #adaug bancnotele de la clienti in stoc
    for b in bancnote_client:
        for bancnota in bancnote_disponibile:
            if bancnota['valoare'] == b:
                bancnota['stoc'] += 1
                break
    return bancnote_disponibile

def simulare(data):
    bancnote = data["bancnote"]
    produse = data["produse"]
    id_client = 1

    valori_bancnote = [b['valoare'] for b in bancnote]

    while True:
        # aleg un produs random pe care îl va cumpăra clientul, iar apoi
        produs = random.choice(produse)
        pret = produs["pret"]
        suma=randint(pret,pret+20)
        rest=suma-pret

        #bancnote_client = random.choices(valori_bancnote, k=random.randint(1, 5))
        #clientul plătește cu bancnote
        #bancnote_client, suma = genereaza_bancnote_client(valori_bancnote, pret)
        #rest = suma - pret


        print(f"\nClient #{id_client}")
        print(f"Produs: {produs['nume']} (Preț: {pret} lei)")
        print(f"Suma plătită de client: {suma} lei")
        #print(f"Bancnotele oferite: {bancnote_client}")
        print(f"Rest de dat: {rest} lei")

        # adaug bancnotele primite în casa de marcat
        #bancnote = adauga_bancnote_in_stoc(bancnote, bancnote_client)

        bancnote, combinatie = calculeaza_rest(bancnote, rest)

        if combinatie == 0:
            print("Nu se mai poate da rest. Oprire...")
            break
        else:
            print("Rest oferit:")
            afiseaza_rest(bancnote, combinatie)

        id_client += 1

if __name__ == '__main__':
    date = citeste_date("date.json")
    simulare(date)
