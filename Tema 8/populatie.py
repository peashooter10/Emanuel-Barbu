import random
import csv

lista = [[] for _ in range(1000)]
data=[]

def generare_judete():
    nume_judete=[
        "Alba", "Arad", "Argeș", "Bacău", "Bihor", "Bistrița-Năsăud", "Botoșani", "Brăila", "Brașov", "Buzău",
        "Călărași", "Caraș-Severin", "Cluj", "Constanța", "Covasna", "Dâmbovița", "Dolj", "Galați", "Giurgiu", "Gorj",
        "Harghita", "Hunedoara", "Ialomița", "Iași", "Ilfov", "Maramureș", "Mehedinți", "Mureș", "Neamț", "Olt",
        "Prahova", "Sălaj", "Satu Mare", "Sibiu", "Suceava", "Teleorman", "Timiș", "Tulcea", "Vâlcea", "Vaslui",
        "Vrancea","București"
    ]
    judet_final=random.randint(0,42)
    judet_final+=1
    return judet_final

def generare_an():
    categorii_de_varsta=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
    probabilitate=[5.02,5.37,5.74,5.45,5.00,5.03,6.53,6.53,7.62,7.70,8.74,5.30,6.40,6.63,5.20,3.23,1.93]
    categorie=random.choices(categorii_de_varsta,weights=probabilitate)[0]
    varsta=random.randint(max(0,categorie-4),categorie)
    an_final=(2025-varsta)
    return an_final

def generare_luna_zi():
    luna=random.randint(1,12)
    lungime_luna=random.choices([28,30,31],weights=[1,7,4])[0]
    if lungime_luna==28:
        luna_finala=2
        zi_finala=random.randint(1,28)
    if lungime_luna==30:
        luna_finala=random.choice([4,6,9,11])
        zi_finala = random.randint(1, 30)
    if lungime_luna==31:
        luna_finala=random.choice([1,3,5,7,8,10,12])
        zi_finala = random.randint(1, 31)
    return luna_finala,zi_finala

def generare_sex():
    sex=random.choices([1,2],[48.56,51.48])[0]
    strain=random.choices([0,7],[99,1])[0]
    sex=sex+strain
    return sex

def generare_nume(x):
    nume_familie = [
        "Popescu", "Ionescu", "Dumitrescu", "Constantinescu", "Gheorghiu", "Stan", "Radu", "Munteanu", "Stefan",
        "Dobre",
        "Marin", "Tudor", "Florea", "Radulescu", "Filip", "Ilie", "Sandu", "Barbu", "Chiriac", "Voicu",
        "Badea", "Petrescu", "Neagu", "Balan", "Mihai", "Serban", "Enache", "Cristea", "Dragan", "Stoica",
        "Nistor", "Lazar", "Mocanu", "Vlad", "Albu", "Dinu", "Roman", "Miron", "Lungu", "Ciobanu",
        "Oprea", "Andreescu", "Baciu", "Sava", "Ignat", "Iacob", "Matei", "Pavel", "Rosu", "Bucur",
        "Paraschiv", "Voinea", "Georgescu", "Dragomir", "Toma", "Zamfir", "Tudose", "Dascalescu", "Chirila", "Grigore",
        "Pana", "Apostol", "Cojocaru", "Anghel", "Nedelcu", "Dima", "Maxim", "Ciuca", "Preda", "Badescu",
        "Cimpeanu", "Cazacu", "Boboc", "Banu", "Busuioc", "Pascu", "Mitrea", "Manole", "Hosu", "Ene",
        "Cazan", "Puscasu", "Talpes", "Vasilescu", "Simion", "Moraru", "Visan", "Costache", "Nita", "Savulescu"
    ]
    nume_baieti = [
        "Andrei", "Alexandru", "Mihai", "Stefan", "Gabriel", "Florin", "Cristian", "Ion", "Daniel", "Radu",
        "Vlad", "Victor", "George", "Razvan", "Ionut", "Darius", "Paul", "Tudor", "Bogdan", "Cosmin",
        "Marian", "Dragos", "Eduard", "Lucian", "Sorin", "Ovidiu", "Silviu", "Emanuel", "Claudiu", "Adrian",
        "Nicu", "Laurentiu", "Horia", "Calin", "Octavian", "Sergiu", "Dumitru", "Petru", "Robert", "Valentin",
        "Sebastian", "Cornel", "Marius", "Damian", "Alin", "Eusebiu", "Filip", "Constantin", "Grigore", "Emil"
    ]
    nume_fete = [
        "Maria", "Andreea", "Elena", "Ioana", "Gabriela", "Ana", "Alexandra", "Cristina", "Larisa", "Diana",
        "Roxana", "Ramona", "Daniela", "Loredana", "Monica", "Simona", "Alina", "Adriana", "Evelina", "Nicoleta",
        "Mirela", "Georgiana", "Irina", "Bianca", "Lavinia", "Anca", "Mihaela", "Delia", "Carmen", "Beatrice",
        "Iuliana", "Camelia", "Luiza", "Raluca", "Corina", "Teodora", "Lidia", "Oana", "Mariana", "Valentina",
        "Anisoara", "Emilia", "Sorina", "Felicia", "Tatiana", "Amalia", "Liliana", "Florentina", "Ioanina", "Doina"
    ]
    if x==1:
        nume = [random.choice(nume_familie) + " " + random.choice(nume_baieti)]
    else:
        nume = [random.choice(nume_familie) + " " + random.choice(nume_fete)]
    return nume

def generare_cnp():

    an=generare_an()
    sex=generare_sex()
    nume=generare_nume(sex)
    if an>1999 and sex<3:
        sex+=4
    an=an%100
    luna,zi=generare_luna_zi()
    judet=generare_judete()
    n1=random.randint(0,9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)

    if luna<10:
        luna1=0
        luna2=luna
    else:
        luna1=luna//10
        luna2=luna%10
    if zi<10:
        zi1=0
        zi2=zi
    else:
        zi1=zi//10
        zi2=zi%10
    if judet<10:
        judet1=0
        judet2=judet
    else:
        judet1=judet//10
        judet2=judet%10

    cifra_de_control=0
    s=(sex*1+(an//10)*2+(an%10)*3+luna1*4+luna2*5+zi1*6+zi2*7+judet1*8+judet2*9+n1*10+n2*11+n3*12)%11
    if s<10:
        cifra_de_control=s
    else:
        cifra_de_control=1
    s = [sex, an // 10, an % 10, luna1, luna2, zi1, zi2, judet1, judet2, n1, n2, n3, cifra_de_control]
    sir = ''.join(str(x) for x in s)

    return sir,nume

def creare_date():
    with open("date_cnp.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for i in range(1000000):
            cnp, nume = generare_cnp()
            writer.writerow([cnp, nume[0]])

def hashing(cnp):
    a1=int(cnp[0:3])
    a2=int(cnp[3:6])
    a3=int(cnp[6:9])
    a4=int(cnp[9:12])
    a5=int(cnp[12:13])
    s=(a1+a2+a3+a4+a5)%1000
    return s

def citire_atribuire():
    global data
    with open("date_cnp.csv", mode="r", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        data = reader
        for row in reader:
            cnp=row[0]
            nume=row[1]
            poz=hashing(cnp)
            lista[poz].append((cnp, nume))

def check():
    citire_atribuire()
    for i in range(1000):
        print(f"{i}: {len(lista[i])}")

def random_cnp():
    val=random.randint(1,1000000)
    return data[val]

def cautare():
    c=0
    for j in range(1000):
        cnp,nume=random_cnp()
        s=hashing(cnp)
        for i in range(0,len(lista[s])):
            if (cnp,nume)==lista[s][i]:
                c+=i
                print(i)
    print(c)

random_cnp()




