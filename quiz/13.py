def my_function(sir):
    for j in range(0,20):
        for i in range(0, len(sir)):
            if (i+1)%3==0:
                print(sir[i],end="")
