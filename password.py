import sys
import string
import numpy as np


def setup(opt, fg=0, var=1):
    sp = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
    ]

    fd = {'u':1, 'l':2, 'd':4, 'p':8,}
    
    for item in opt:
        fg += fd.get(item, 0)

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


def random_choice(arg, weight):
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


def main(lg, un, wg, pw='', pwl=[]):
    for i in range(lg):
        pwl.append(random_choice(un, wg))

    pw = pw.join(pwl)
  
    return pw


if __name__ == '__main__':
    lenght, mode = set_options(sys.argv[1:])
    universe = setup(mode)
    weight = set_weight(universe)
    password = main(lenght, universe, weight)
    print(password)