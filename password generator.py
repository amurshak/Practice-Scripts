
import random
import string
from string import punctuation


user_pass = str(input('Password:'))

#Chooses random characters from a list of uppercase, lowercase, and punctuation characters.
characters = list(string.ascii_lowercase + string.ascii_uppercase +string.punctuation)


def scrambler(password):
    encrypted = ''
    for char in password:
        encrypted += (random.choice(characters))
    return encrypted

scrambler(user_pass)

