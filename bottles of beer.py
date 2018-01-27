#Bottles of Beer by Alex Murshak
#counts down from i bottles of beer to 0

i = 20
while i>1:
    print(i,"bottles of beer on the wall!")
    print(i, "bottles of beer!")
    print("take one down, pass it around.")
    if i-1>1:
        print(i-1, "bottles of beer!")
    else:
         print(i-1, "bottle of beer!")
    print("")
    i -= 1
print(i,"bottle of beer on the wall")
print(i, "bottle of beer!")
print("take one down, pass it around.")
print("No, bottles of beer on the wall!")

