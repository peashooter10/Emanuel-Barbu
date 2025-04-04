import matplotlib.pyplot as plt
import csv
from populatie import hashing
import numpy as np

l_sex = [0, 0]
l_an = [0] * 2030
l_luna = [0] * 13
l_zi = [0] * 32
l_judet = [0] * 50
l_hash = [0] * 1001

def extragere_informatii(cnp):
    sex = int(cnp[0])
    if sex == 5 or sex == 6:
        an_base = 2000
    else:
        an_base = 1900
    sex = sex % 2
    an = an_base + int(cnp[1:3])
    luna = int(cnp[3:5])
    zi = int(cnp[5:7])
    judete = int(cnp[7:9])

    return sex, an, luna, zi, judete

def date():
    global l_sex, l_an, l_luna, l_zi, l_judet, l_hash
    with open("date_cnp.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if not row:
                continue

            cnp = row[0]
            sex, an, luna, zi, judete = extragere_informatii(cnp)
            cod_hash = hashing(cnp)

            l_sex[sex] += 1
            l_an[an]+=1
            l_luna[luna]+=1
            l_zi[zi]+=1
            l_judet[judete]+=1
            l_hash[cod_hash]+=1

    return l_sex, l_an, l_luna, l_zi, l_judet, l_hash

def distributie_hash(h):
    numere = range(1001)
    plt.figure(figsize=(10, 5))
    plt.bar(numere, h, color='black', alpha=0.7, width=1)
    plt.xlabel('Valori hash')
    plt.ylabel('Frecvență')
    plt.title('Distribuție hash')
    plt.show()

def distributie_sex(s):
    labels = ['Femei', 'Bărbați']
    plt.figure(figsize=(5, 5))
    plt.pie(s, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'blue'])
    plt.title('Distribuție sex')
    plt.show()

def distributie_an(a):
    numere = range(1930,2030)
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(numere, a[:len(numere)], color='black', alpha=0.7, width=0.8)

    ax.set_xlabel('An')
    ax.set_ylabel('Frecvență')
    ax.set_title('Distribuție ani')

    plt.xticks(rotation=45)

    plt.show()

def distributie_luna(l):
    numere = range(1, 13)
    plt.figure(figsize=(7, 5))
    plt.bar(numere, l, color='black', alpha=0.7, width=0.8)
    plt.xlabel('Lunile anului')
    plt.ylabel('Frecvență')
    plt.title('Distribuție luni')
    plt.xticks(numere)
    plt.show()

def distributie_zi(z):
    numere = range(1, 32)
    plt.figure(figsize=(10, 5))
    plt.bar(numere, z, color='black', alpha=0.7, width=0.8)
    plt.xlabel('Zi')
    plt.ylabel('Frecvență')
    plt.title('Distribuție zi')
    plt.xticks(numere)
    plt.show()

def distributie_judet(j):
    numere = range(1, 43)
    plt.figure(figsize=(10, 5))
    plt.bar(numere, j, color='black', alpha=0.7, width=0.8)
    plt.xlabel('Județe')
    plt.ylabel('Frecvență')
    plt.title('Distribuție județe')
    plt.xticks(numere)
    plt.show()

def arata():
    s, a, l, z, j, h = date()
    while True:
        cod = input("all ").strip().lower()
        if cod == 'all':
            distributie_sex(s)
            distributie_an(a)
            distributie_luna(l)
            distributie_zi(z)
            distributie_judet(j)
            distributie_hash(h)
        elif cod == 'esc':
            print("escape")
            break
        else:
            print("invalid")


distributie_hash()

