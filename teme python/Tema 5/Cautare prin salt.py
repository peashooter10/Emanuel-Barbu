import math
def cauta_container(containere, numar_identificare):
    n=len(containere)
    salt = int(math.sqrt(n))
    st=0
    ok=0
    numar_pasi=0
    for i in range (0,n,salt):
        numar_pasi+=1
        if numar_identificare==containere[i]:
            ok=1
            return(print(f"Containerul cu numărul {numar_identificare} a fost găsit pe pozitia {i} după {numar_pasi} pași."))
        if containere[i]<numar_identificare:
            st=i
        if containere[i]>numar_identificare:
            break
    for i in range(st, min(st+salt,n)):
        numar_pasi+=1
        if numar_identificare==containere[i] and ok==0:
            return(print(f"Containerul cu numărul {numar_identificare} a fost găsit pe pozitia {i} după {numar_pasi} pași."))
    return(print(f"Containerul cu numărul {numar_identificare} nu a fost găsit în sistem. Total pași efectuați: {numar_pasi}."))

