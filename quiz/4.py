def my_function(sir):
    sub="s"
    for i in range(0, len(sir)):
        if sir.count(sub)>0:
            sir=sir.replace(sir[i],"*")
    print(sir)

sir=input()
my_function(sir)
