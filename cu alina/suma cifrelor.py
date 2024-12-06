def suma(n):
    s=0
    while n>0:
        s+=n%10
        n=n//10
    print(s)

numar=int(input())
suma(numar)
