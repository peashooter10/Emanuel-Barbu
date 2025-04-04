import hashlib
import sys
#import csv

sys.setrecursionlimit(10**9)

# Variabile globale
parola = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"
varianta = list("aaaA0!") # Lista inițială, forma parolei pe care vrem să o spargem
caractere = ["!", "#", "@", "$"] # Caracterele speciale
c = 0 # c este contorul pe care îl vom folosi pentru a vedea numărul apelurilor recursive
l=[] # lista goală în care vom avea toate combinațiile posibile
oprire=0

# Deschidem un fișier CSV pentru scriere
#csv_file = open("incercari_parola.csv", "w", newline="", encoding="utf-8-sig")
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(["Număr încercare", "Parolă încercată"]) # Scriem antetul

def get_hash(password):
    # returnează codul hash sha256 al parolei
    return hashlib.sha256(password.encode()).hexdigest()

def crestere(c):
    # Trecem la următorul caracter di categorie
    '''
    De ce avem nevoie de această funcție? Pentru a „crește” caracterul. De exemplu:
    aaaA0! -> aaaA0? -> aaaA0@ -> aaaA0$
    '''
    if "a" <= c < "z":
        return chr(ord(c) + 1)
    if "A" <= c < "Z":
        return chr(ord(c) + 1)
    if "0" <= c < "9":
        return chr(ord(c) + 1)
    if c in caractere:
        return caractere[(caractere.index(c) + 1) % len(caractere)]  # Rotim prin caractere speciale
    return c

def baza(c):
    # Returnez un caracter la „caracterul de bază” din categoria respectivă
    '''
    Folosim această funcție pentru a ne reseta și întoarce un caracter
    aaaA0? -> aaaA1!
    '''
    if "a" <= c <= "z":
        return "a"
    if "A" <= c <= "Z":
        return "A"
    if "0" <= c <= "9":
        return "0"
    if c in caractere:
        return "!"
    return c

def f(varianta, indice, ok):
    global oprire
    global c
    if oprire==0:
        c += 1  # Creștem contorul c
        incercare = "".join(varianta)  # Transformăm lista într-un șir de caractere

        print(f"Attempt {c}: {incercare}")  # Afișează progresul
        #print(incercare)

        # Verificăm dacă am găsit parola
        if str(get_hash(incercare)) == parola:
            oprire = 1
            raise Exception(f"{incercare}")
            indice=-1
            return 0 # Parola a fost găsită, trebuie să oprim recursivitatea

        # Dacă am ajuns la primul caracter și trebuie să îl resetăm, am terminat
        if indice == -1:
            print("Am terminat această combinație.")
            return False  # Am terminat căutarea

        # Logica de creștere
        if ok == 1:
            if varianta[indice] in ["z", "Z", "9", "$"]:
                varianta[indice] = baza(varianta[indice])  # Resetăm caracterul curent
                f(varianta, indice - 1, 0)  # Trecem la caracterul anterior
            else:
                varianta[indice] = crestere(varianta[indice])
                f(varianta, indice, 1)  # Verificăm dacă trebuie să ne oprim
        else:
            if varianta[indice] in ["z", "Z", "9", "$"]:
                varianta[indice] = baza(varianta[indice])
                f(varianta, indice - 1, 0)
            else:
                varianta[indice] = crestere(varianta[indice])
                f(varianta, len(varianta) - 1, 1)  # Verificăm dacă trebuie să ne oprim
    '''
    aaaY9$
    aaaY9!
    aaaY0!
    aaaZ0!
    
    '''

def genPermutation(i, s, used, curr, st):
    if i == len(s):
        # Add the permutation to the result set
        st.add("".join(curr))
        return

    for j in range(len(s)):
        if not used[j]:
            # Mark the character as used
            used[j] = True
            curr.append(s[j])

            # Recurse with the next character
            genPermutation(i + 1, s, used, curr, st)

            # Backtrack and unmark the character
            used[j] = False
            curr.pop()

def findPermutation(s):
    # To track if a character is used
    used = [False] * len(s)
    st = set()
    curr = []

    # Start the recursion
    genPermutation(0, s, used, curr, st)

    # Convert the set to a list
    return list(st)

def main():
    global l
    sir="aaaA0!"
    raspuns=findPermutation(sir)
    raspuns.sort()
    '''
    for i in range(len(raspuns)):
        if raspuns[i] == "Aaaa!0":
            print(i)
    '''
    for i in range(0,len(raspuns)):
        p=list(raspuns[i])
        try:
            f(p,5,1)
        except Exception as e:
            pass
    #csv_file.close()  # Asigurăm închiderea fișierului

def test():
    varianta=['U','a','r','e','#','1']
    incercare = "".join(varianta)
    if get_hash(incercare) == parola:
        print(f"\nParola '{parola}' a fost găsită după {c} încercări.")
    else:
        print("fail")

#main()
f(list("aaaA0!"),5,1)

