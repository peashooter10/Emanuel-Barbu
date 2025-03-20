def f(n):
    a = [[" " for i in range(2 * n + 1)] for j in range(n + 1)]

    for i in range(n):
        for j in range(n):
            a[i][j]="c"
            a[2*n-1-i][n-j-1]="c"

    for i in range(0, 2*n + 1):
        for j in range(0,n):
            print(a[i][j], end=" ")
        print()

f(4)
