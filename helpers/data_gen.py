import random
import string



def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters)
                            for i in range(length))
    return random_string

def create_email():
    name = generate_random_string(7)
    email = f'{name}@gmail.com'
    return email



    