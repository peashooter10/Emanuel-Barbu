def joc():
    import random
    from dataclasses import replace
    from importlib import reload
    from operator import truediv

    #cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
    cuvinte=["amandina", "savarina", "cremes", "eclere", "briosa", "cremes"]
    cuvant_de_ghicit = random.choice(cuvinte)
    progres = ["_" for _ in cuvant_de_ghicit]

    # 2. Inițializarea numărului de încercări
    incercari_ramase = 6
    litere_incercate = []

    alfabet = [0] * 26

    while incercari_ramase > 0:
        litera = input("Te rog sa introduci o litera: ")
        if not litera.isalpha() or len(litera) != 1:
            print("Eroare. Te rog sa introduci o litera: ")
            continue
        else:
            if alfabet[ord(litera) - 97] != 0:
                incercari_ramase = incercari_ramase - 1
                print(f"Ai mai introdus aceasta litera. Mai ai {incercari_ramase} incercari.")
            else:
                k = 0
                alfabet[ord(litera) - 97] = 1
                for i in range(0, len(cuvant_de_ghicit)):
                    if litera == cuvant_de_ghicit[i]:
                        progres[i] = litera
                        k = 1
                if k == 1:
                    print(progres)
                if k == 0:
                    print("Nu ai ghicit litera.")
                    incercari_ramase = incercari_ramase - 1
                    print(f"Mai ai {incercari_ramase} incercari.")

        k=0
        for i in range(0, len(cuvant_de_ghicit)):
            if progres[i] == cuvant_de_ghicit[i]:
                k+=1
        if k==len(cuvant_de_ghicit):
            print(f"Felicitari. Ai ghicit cuvantul: {cuvant_de_ghicit}.")
            incercari_ramase=-1

    if incercari_ramase==0 :
        for i in range(0, len(cuvant_de_ghicit)):
            if progres[i] == cuvant_de_ghicit[i]:
                k += 1
        if k != len(cuvant_de_ghicit):
            print(f"Cuvantul care trebuia ghicit era: {cuvant_de_ghicit}.")

joc()