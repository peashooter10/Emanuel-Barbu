def my_function(sir):
    a=sir[1]
    b=sir[len(sir)-1]
    sir.replace(b,sir[1])
    sir.replace(sir[len(sir)-1],a)
    print(sir)

my_function("String!")