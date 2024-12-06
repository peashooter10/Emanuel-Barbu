def f(n):
    p=1
    while n>0:
        if (n%10)%2!=0:
            p=p*(n%10)
        n=n//10
    print(p)
f(2531)
