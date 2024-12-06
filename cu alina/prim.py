def prim(n):
    if n==0 or n==1:
        print("nu e prim")
    else:
        c=0
        for i in range(1,n+1):
            if n%i==0:
                c+=1
        if c==2:
            print(f"{n} e prim")
        else:
            print(f"{n} nu e prim")

numar=int(input())
prim(numar)
