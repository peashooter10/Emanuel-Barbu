def vocale(sir):
    v="aeiouAEIOU"
    c=0
    for i in range(0,len(sir)):
        for j in range(0, len(v)):
            if sir[i]==v[j]:
                c+=1
    print(c)

s=str(input())
vocale(s)