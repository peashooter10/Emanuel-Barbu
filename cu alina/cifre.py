def numara_cifre(n):
    s=0
    if n<10:
        s=1
    else:
        while n>0:
            s=s+1
            n=n//10
    return s
print(numara_cifre(987654321))

