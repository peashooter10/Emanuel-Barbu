import random

def numar_regine(n):
    tabla=[]
    for i in range(n+1):
        for j in range(n+1):
            if i==0 or i==n or j==0 or j==n:
                tabla[i][j]=2
            else:
                tabla[i][j]=1

    for i in range(1,n+1):
        if i==1:
            val = random.randint(1, n)
        elif 1<i and i<n:
            while tabla[i][val]!=0 and tabla[i-1][val]!=0 and tabla[i-1][val-1]!=0 and tabla[i-1][val+1]!=0:
                val=random.randint(1,n)
        tabla[i][val] = 1
        tabla[i + 1][val - 1] = 2
        tabla[i + 1][val] = 2
        tabla[i + 1][val + 1] = 2

    for i in range(1, n):
        for j in range(0, n):
            print(tabla[i][j], end=" ")
        print()

if __name__ == '__main__':
    numar_regine(8)