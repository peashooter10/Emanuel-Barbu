def my_function(sir,sub):
    val=0
    for i in range(0, len(sir)):
        if sir[i]=="s":
            val=i
            print(val)
            break
    sir=sir[0:val+1]+sir[val+1:].replace(sir[i],"*")
    print(sir)

my_function("student senator", "s")


