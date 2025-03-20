def numere_cu_k_divizori(l, k):
    a=[]
    for i in range(0,len(l)):
        c=0
        for j in range(1,i+1):
            if i % j == 0:
                c += 1
        if c==k:
            a.append(i)
        print(a)


