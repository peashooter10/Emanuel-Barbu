sir=input()
vocale="aeiouAEIOU"
c=0
for i in range(0,len(sir)):
    for j in range(0,len(vocale)):
        if sir[i]==vocale[j]:
            c=c+1
print(c)
