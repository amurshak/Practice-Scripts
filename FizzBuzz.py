#FizzBuzz
#A solution to the notorious "FizzBuzz" coding interview problem.
#
#
#Formal statement of problem from HackerRank.com:
#Write a short program that prints each number from 1 to 100 on a new line. 
#For each multiple of 3, print "Fizz" instead of the number. 
#For each multiple of 5, print "Buzz" instead of the number.
#For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
#
#Solution by Alex Murshak


def fizzer(b):
    return print(b,"Fizz")

def buzzer(b):
    return print(b,"Buzz")

def FizzyBuzzer(b):
    return print(b,"FizzBuzz")


if __name__=='__main__':
    for n in range(1,101):
        if n%3==0 and n%5==0:
            FizzyBuzzer(n)
        elif n%3==0:
            fizzer(n)
        elif n%5==0:
            buzzer(n)
