import sys
import string
import numpy as np

def setup(opt, fg=0, var=1):
    
    if 'u' in opt:
        fg+=1
    
    if 'l' in opt:
        fg+=2
    
    if 'd' in opt:
        fg+=4

    if 'p' in opt:
        fg+=8

    sp = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
    ]

    for item in sp.copy():
        f = fg & var
        if f != 0:
            sp.remove(item)
        var = var << 1
    
    return sp


def set_weight(arg):
    if len(arg) == 4:
        wg = [0.35, 0.35, 0.15, 0.15]
    elif len(arg) == 3:
        wg = [0.5, 0.3, 0.2]
    elif len(arg) == 2:
        wg = [0.7, 0.3]
    else:
        wg = [1]

    return wg


def random_choice(arg, weight=None):
    gr = np.random.choice(arg, 1, p=weight)
    cr = np.random.choice(list(*gr))

    return cr


def set_options(opt, l=8, m=''):
    if any([x.startswith('-t') for x in opt]):
        pre = list(filter(lambda x: x.startswith('-t'), opt))
        l = int(pre[0].split('-t')[1])
        opt.remove(*pre)
    
    if any([x.startswith('-') for x in opt]):
        pre = list(filter(lambda x: x.startswith('-'), opt))
        m = pre[0].split('-')[1]
        opt.remove(*pre)

    return l, m


def main(pw='', pwl=[]):
    lenght, mode = set_options(sys.argv[1:])
    universe = setup(mode)
    weight = set_weight(universe)

    for i in range(lenght):
        pwl.append(random_choice(universe, weight))

    pw = pw.join(pwl)
  
    return pw


if __name__ == '__main__':
    password = main()
    print(password)