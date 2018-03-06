#! python3
# Author: rojojojo (Rohan)
# pswgenerator.py - Python script to generate a complex password

import random
import argparse
import string
import pyperclip
from random import choice

parser = argparse.ArgumentParser(description="Python script to generate a complex password that includes "
                                             "uppercase and lowercase characters, numbers, and special characters. "
                                             "The -l flag denotes the length of the password. By default, the "
                                             "script will generate an 8 character complex password.")
parser.add_argument("-l", dest='length', help="Length of the password", nargs='?', const=8, default=8)
args = parser.parse_args()


def lengthcheck(l1):
    while l1 < 7:
        print('Minimum password length is 8')
        l1 = input('Enter length of password: ')
        l1 = int(l1)
    return l1


def pswgen(l1):
    l1 = l1 - 4
    password = ''
    psw = random.choice(chars) + random.choice(chars.upper()) + random.choice(numbers) + random.choice(special_chars)
    password = password + psw
    characters = string.ascii_letters + string.punctuation + string.digits
    for i in range(l1):
        psw = choice(characters)
        password = password + psw
    a = list(password)
    random.shuffle(a)
    b = ''.join(a)
    print('The password is: ' + b)
    print('Password copied to clipboard')
    pyperclip.copy(b)


try:
    length = int(str(args.length))
    chars = string.ascii_lowercase
    numbers = string.digits
    special_chars = string.punctuation
    if length != 'None':
        print('-------Random Password Generator-------')
        length = lengthcheck(length)
        pswgen(length)
    else:
        pswgen(8)
except:
    print('Invalid entry. Please execute the script again')
