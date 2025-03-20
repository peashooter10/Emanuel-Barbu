def p_273(l):
    sume = set()
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            sume.add(l[i] + l[j])  # Add the sum of two distinct elements
    print(sorted(sume))  # Return the sorted list of sums
p_273('13 11 13 134 14 33 555')