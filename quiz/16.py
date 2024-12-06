def my_function(sir):
    for i in range(0, len(sir)):
        for j in range(i+1, len(sir)):
            if sir[i]<sir[j]:
                sir[i],sir[j]=sir[j],sir[i]
    print(sir)
        