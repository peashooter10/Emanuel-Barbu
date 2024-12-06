def my_function(sir):
    for i in range(0, len(sir)):
        if i%2==0:
            print(sir[i],end="")
sir=input()
my_function(sir)