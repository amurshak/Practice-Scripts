
    
        

num = int(input("Pick a limit:"))

for n in range(1, num+1):
    square = str(n**2)

    for i in range(1, len(square)):
        a, b = int(square[:i]), int(square[i:])

        if a + b == n and a != 0 and b != 0:
            print (n)
