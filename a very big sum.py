

ar = [5,
1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

def aVeryBigSum(ar):
    total = 0
    for i in ar:
        total += i
    return total

print(aVeryBigSum(ar))
