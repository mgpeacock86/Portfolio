from math import comb

def Chances(n, x, a):
    results = comb(n-x, a) / comb(n/a)
    results = round(results, 5)
    return print(results)

