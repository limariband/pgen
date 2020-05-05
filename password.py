import string
import click
import numpy as np


def setup(digit, upper, lower, punct):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = '!#$%&*+-.?@_'

    stp = [
        uppercase,
        lowercase,
        digits,
        punctuation, 
    ]

    if digit:
        stp.remove(digits)    
    if upper:
        stp.remove(ascii_uppercase)
    if lower:
        stp.remove(ascii_lowercase)    
    if punct:
        stp.remove(punctuation)
    return stp


def set_weight(args):
    if len(args) == 4:
        weight = [0.35, 0.35, 0.15, 0.15]
    elif len(args) == 3:
        weight = [0.5, 0.3, 0.2]
    elif len(args) == 2:
        weight = [0.7, 0.3]
    else:
        weight = [1]
    return weight


def verify(password, universe):
    v = {}
    for item in universe:        
        if item[0].islower():
            v.update({'l':0})
        elif item[0].isupper():
            v.update({'u':0})
        elif item[0].isdigit():
            v.update({'d':0})
        else:
            v.update({'p':0})

    for char in password:
        if char.islower():
            v['l'] += 1
        elif char.isupper():
            v['u'] += 1
        elif char.isdigit():
            v['d'] += 1
        else:
            v['p'] += 1
    
    flag = not all([bool(x) for x in v.values()])    
    return flag


def set_password(context, lenght, weigth):
    password = ''
    for i in range(lenght):
        password += random_choice(context, weigth)
    return password


def random_choice(args, weight):
    group = np.random.choice(args, 1, p=weight)
    character = np.random.choice(list(*group))
    return character


@click.command(context_settings={'help_option_names':['-h','--help']})
@click.version_option('1.0.0')
@click.option('--lenght', type=int, default=8, 
    show_default=True, help='Password lenght')
@click.option('-d', '--no-digit', is_flag=True,
    default=False, help='Password is generated without numbers')
@click.option('-u', '--no-upper', is_flag=True,
    default=False, help='Password is generated without uppercases')
@click.option('-l', '--no-lower', is_flag=True,
    default=False, help='Password is generated without lowercases')
@click.option('-p', '--no-punct', is_flag=True,
    default=False, help='Password is generated without punctuation')
def get_password(lenght, no_digit, no_upper, no_lower, no_punct):
    uni = setup(no_digit, no_upper, no_lower, no_punct)
    wgt = set_weight(uni)
    pwd = set_password(uni, lenght, wgt)
    while (verification:=verify(pwd, uni)):
        pwd = set_password(uni, lenght, wgt)
    print(pwd)


if __name__ == '__main__':
    get_password()