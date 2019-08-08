import numpy as np


def compareTriplets(a, b):
    c = [0, 0]

    for i in range(3):
            if a[i]>b[i]:
                c[0] += 1
            if a[i]<b[i]:
                c[1] +=1
            else:
                pass
    return c
       

a = [5,6,7]
b = [3,6,19]

print(compareTriplets(a,b))
