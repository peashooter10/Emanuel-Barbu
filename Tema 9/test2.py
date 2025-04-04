# cerința? spargerea unei parole :)
'''
Ce știm despre parolă?
    Parola conține 3 litere mici, o literă mare, o cifră și un caracter special(!,?,@,$).
Cum o spargem?
    Backtracking :O
    Asta include să încercăm și să generăm toate cazurile posibile.
'''

import hashlib
import sys

sys.setrecursionlimit(10**9)

# Variabile globale
parola = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"
varianta = list("aaaA0!") # Lista inițială, forma parolei pe care vrem să o spargem
caractere = ["!", "?", "@", "$"] # Caracterele speciale
c = 0 # c este contorul pe care îl vom folosi pentru a vedea numărul apelurilor recursive
l=[] # lista goală în care vom avea toate combinațiile posibile

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
    # Funcție recursivă pentru a genera toate valorile posibile

    global c
    c += 1 # Creștem contorul c

    incercare = "".join(varianta) # Transformăm lista într-un șir de caractere

    print(f"Attempt {c}: {incercare}")# Afișează progresul

    # Verificăm dacă am găsit parola
    if get_hash(incercare) == parola:
        print(f"\nParola '{parola}' a fost găsită după {c} încercări.")
        return True

    # Dacă am ajuns la primul caracter și trebuie să îl resetăm, am terminat
    if indice == -1:
        print("Am terminat această combinație.")
        return False

    # Logica de creștere
    if ok == 1:
        if varianta[indice] in ["z", "Z", "9", "$"]:
            varianta[indice] = baza(varianta[indice])  # Resetăm caracterul curent
            return f(varianta, indice - 1, 0)  # Trecem la caracterul anterior
        else:
            varianta[indice] = crestere(varianta[indice])
            return f(varianta, indice, 1)
    else:
        if varianta[indice] in ["z", "Z", "9", "$"]:
            varianta[indice] = baza(varianta[indice])
            return f(varianta, indice - 1, 0)
        else:
            varianta[indice] = crestere(varianta[indice])
            return f(varianta, len(varianta) - 1, 1)  # Resetăm la ultimul caracter

'''
Care e logica programului?
                    
                        /
                    ok=1
                    /   \
f(varianta,indice,ok)
                    \
                    ok=0
'''

def permutari(lista):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return [lista]

    l = []  # Initialize l locally to avoid using the global variable
    for i in range(len(lista)):
        elem = lista[i]
        rest_lista = lista[:i] + lista[i + 1:]

        for p in permutari(rest_lista):
            l.append([elem] + p)

    return l

def main():
    data = list("aaaA0!")
    for p in permutari(data):
        f(p,5,1)

main()