import random

print('Welcome to your password generator')

chars = 'abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ!@#$%&*^().,0123456789?'

number = input('Amount of password to generate:')
number = int(number)

lenght = input('Password lenght:')
lenght = int(lenght)

print('Where are your passwords?:')

for pwd in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
        print(password)