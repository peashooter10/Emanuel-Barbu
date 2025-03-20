def p_1013(l):
    an_minim = 10000
    an_maxim = 0

    for i in range(len(l)):
        if l[i][0] > an_maxim:
            an_maxim = l[i][0]
        if l[i][0] < an_minim:
            an_minim = l[i][0]

    luna_maxim = 0
    luna_minim = 13
    for i in range(len(l)):
        if l[i][0] == an_maxim:
            if l[i][1] > luna_maxim:
                luna_maxim = l[i][1]
        if l[i][0] == an_minim:
            if l[i][1] < luna_minim:
                luna_minim = l[i][1]

    zi_maxim = 0
    zi_minim = 32
    for i in range(len(l)):
        if l[i][0] == an_maxim and l[i][1] == luna_maxim:
            if l[i][2] > zi_maxim:
                zi_maxim = l[i][2]
        if l[i][0] == an_minim and l[i][1] == luna_minim:
            if l[i][2] < zi_minim:
                zi_minim = l[i][2]

    for i in range(len(l)):
        if l[i][0] == an_maxim and l[i][1] == luna_maxim and l[i][2] == zi_maxim:
            print(i + 1)

    for i in range(len(l)):
        if l[i][0] == an_minim and l[i][1] == luna_minim and l[i][2] == zi_minim:
            print(i + 1)


p_1013([[2003, 12, 17], [2011, 1, 12], [2003, 12, 19], [2011, 6, 29], [2011, 6, 30]])