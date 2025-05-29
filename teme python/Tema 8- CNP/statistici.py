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
    #extragem anul in care s-a nascut cineva
    if sex == 5 or sex == 6:
        an_base = 2000
    else:
        an_base = 1900
    sex = sex % 2
    an = an_base + int(cnp[1:3])

    # extragem luna, zi, judet
    luna = int(cnp[3:5])

    zi = int(cnp[5:7])
    judete = int(cnp[7:9])

    # check la luna
    if not (1 <= luna <= 12):
        print(f"atentie, luna gresita")

    return sex, an, luna, zi, judete

def date():
    global l_sex, l_an, l_luna, l_zi, l_judet, l_hash

    #resetam counterele
    l_sex = [0, 0]
    l_an = [0] * 2030
    l_luna = [0] * 13
    l_zi = [0] * 32
    l_judet = [0] * 50
    l_hash = [0] * 1001

    record_count = 0
    invalid_months = 0

    try:
        with open("date_cnp.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if not row:
                    continue

                cnp = row[0]
                sex, an, luna, zi, judete = extragere_informatii(cnp)
                cod_hash = hashing(cnp)

                l_sex[sex] += 1

                # verific ca anul sa fie corect
                if 1900 <= an < 2030:
                    l_an[an] += 1

                # verific daca luna este corecta
                if 1 <= luna <= 12:
                    l_luna[luna] += 1
                else:
                    invalid_months += 1

                if 1 <= zi <= 31:
                    l_zi[zi] += 1

                if 1 <= judete <= 49:
                    l_judet[judete] += 1

                if 0 <= cod_hash <= 1000:
                    l_hash[cod_hash] += 1

                record_count += 1

        # afisez date din cvs
        print(f"S-au procesat {record_count} date din fisierul csv")
        if invalid_months > 0:
            print(f"S-au gasit {invalid_months} date cu luni nevalide")

    except Exception as e:
        print(f"Eroare: {e}")

    return l_sex, l_an, l_luna, l_zi, l_judet, l_hash

def distributie_hash(h):
    plt.figure(figsize=(10, 5))
    plt.bar(range(1001), h, color='black', alpha=0.7, width=1)
    plt.xlabel('Valori hash')
    plt.ylabel('Frecvență')
    plt.title('Distribuție hash')
    plt.show()

def distributie_sex(s):
    labels = ['Femei', 'Bărbați']
    plt.figure(figsize=(5, 5))

    # vedem daca există date
    if sum(s) > 0:
        plt.pie(s, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'blue'])
        plt.title('Distribuție sex')
    else:
        plt.text(0.5, 0.5, 'No data available', horizontalalignment='center', verticalalignment='center')

    plt.show()

def distributie_an(a):
    # iau numai anii in care s-a nascut cineva
    years = []
    counts = []

    for year in range(1930, 2030):
        if a[year] > 0:
            years.append(year)
            counts.append(a[year])

    if not years:  # daca nu există ani
        plt.figure(figsize=(10, 5))
        plt.text(0.5, 0.5, 'Nu exista date', horizontalalignment='center', verticalalignment='center',transform=plt.gca().transAxes)
        plt.title('Distribuție ani')
        plt.show()
        return

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(years, counts, color='black', alpha=0.7, width=0.8)
    ax.set_xlabel('An')
    ax.set_ylabel('Frecvență')
    ax.set_title('Distribuție ani')

    # limitez numarul de ani pentru a evita prea multe date
    step = max(1, len(years) // 20)
    plt.xticks(years[::step], rotation=45)

    plt.tight_layout()  # ajusteaza spațiu
    plt.show()

def distributie_luna(l):
    plt.figure(figsize=(7, 5))

    months = range(1, 13)
    month_counts = [l[m] for m in months]

    #print("Luna:", month_counts)
    #print("Inregistrari:", sum(month_counts))

    plt.bar(months, month_counts, color='black', alpha=0.7, width=0.8)
    plt.xlabel('Lunile anului')
    plt.ylabel('Frecvență')
    plt.title('Distribuție luni')
    plt.xticks(months)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def distributie_zi(z):
    plt.figure(figsize=(10, 5))

    # Filter out index 0 which is unused
    days = range(1, 32)
    day_counts = z[1:32]

    plt.bar(days, day_counts, color='black', alpha=0.7, width=0.8)
    plt.xlabel('Zi')
    plt.ylabel('Frecvență')
    plt.title('Distribuție zi')
    plt.xticks(days)
    plt.show()

def distributie_judet(j):
    counties = []
    counts = []

    for county in range(0, 43):
        if j[county] > 0:
            counties.append(county)
            counts.append(j[county])

    if not counties:  # If no data
        plt.figure(figsize=(10, 5))
        plt.text(0.5, 0.5, 'Nu exista date', horizontalalignment='center', verticalalignment='center',
                 transform=plt.gca().transAxes)
        plt.title('Distribuție județe')
        plt.show()
        return

    plt.figure(figsize=(10, 5))
    plt.bar(counties, counts, color='black', alpha=0.7, width=0.8)
    plt.xlabel('Județe')
    plt.ylabel('Frecvență')
    plt.title('Distribuție județe')
    plt.xticks(counties)
    plt.show()

def arata():
    try:
        s, a, l, z, j, h = date()
        print("Datele s-au incarcat. Tasteaza all pentru a avea distributiile sau esc pentru a iesi.")

        while True:
            cod = input("Command: ").strip().lower()
            if cod == 'all':
                print("sex...")
                distributie_sex(s)
                print("ani...")
                distributie_an(a)
                print("luna...")
                distributie_luna(l)
                print("zi...")
                distributie_zi(z)
                print("judete...")
                distributie_judet(j)
                print("hash...")
                distributie_hash(h)
            elif cod == 'sex':
                distributie_sex(s)
            elif cod == 'an':
                distributie_an(a)
            elif cod == 'luna':
                distributie_luna(l)
            elif cod == 'zi':
                distributie_zi(z)
            elif cod == 'judet':
                distributie_judet(j)
            elif cod == 'hash':
                distributie_hash(h)
            elif cod == 'esc':
                print("Iesire...")
                break
            else:
                print("Invalid. Foloseste 'all', 'sex', 'an', 'luna', 'zi', 'judet', 'hash', sau 'esc'.")
    except Exception as e:
        print(f"Eroare in functia arata(): {e}")

arata()