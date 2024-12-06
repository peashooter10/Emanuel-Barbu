def palindrom(n):
    nr=n
    p=0
    while n>0:
        cifra=n%10
        p=p*10+cifra
        n=n//10
    if nr==p:
        print("da")
    else:
        print("nu")

nr=int(input())
palindrom((nr))