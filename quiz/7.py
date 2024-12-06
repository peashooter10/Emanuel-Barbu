def my_function(sir, n):
    for i in range(0,n-1):
        print(sir[i],end="")
    for i in range(n, len(sir)):
        print(sir[i],end="")
my_function('String!', 5)
