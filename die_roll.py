import random
print("Welcome to Die Roll")
answer = ""
while True:
    num = random.randint(1,6)
    answer = str(input("Would you like to roll?"))
    if answer == "yes" or answer =="Yes":
        print(num)
    elif answer == "no" or answer == "No":
        break
        
    else:
        print("Invalid input. Please roll again.")
