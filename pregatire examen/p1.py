#Scrieţi o funcție care primește un număr natural n şi construieşte o matrice cu n linii şi n coloane, numerotate de la 1 la n, în care fiecare element aflat pe chenarul exterior al matricei este egal cu suma dintre indicele liniei şi indicele coloanei pe care se află, iar fiecare dintre celelalte elemente este egal cu suma celor trei “vecini” situaţi în matrice pe linia anterioară.
def p(n):
    a = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for j in range(1, n + 1):
        a[1][j] = 1 + j
        a[n][j] = n + j
    for i in range(1, n + 1):
        a[i][1] = 1 + i
        a[i][n] = n + i
    for i in range(2, n):
        for j in range(2, n):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j] + a[i - 1][j + 1]
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(a[i][j], end=" ")
        print("")

p(4)
