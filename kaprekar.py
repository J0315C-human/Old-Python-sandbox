"""kaprekar konstants in other bases.""" 


def dec_to_x(n, x):
    """n in base ten, to base x"""
    if type(n) == str:
        n = int(n)
    new_str = ""
    inc = 0
    while True:
        inc += 1
        a = n%(x**inc)
        n = n - a
        if a != 0:
            a = a / (x**(inc-1))

        a = int(a)
        if a >= 10:
            a = chr(a + 55)
        new_str = str(a) + new_str
        
        if n == 0:
            break
    return new_str

def x_to_dec(n, x):
    """base x str or int,  to base ten"""
    n = str(n).upper()
    new_int = 0
    inc = 0
    for char in n[::-1]:
        if ord(char) >= 65:
            char = ord(char) - 55
        new_int += (int(char)*(x**inc))
        inc += 1

    return new_int

def kap(x, base=10):
    """takes string or int"""
    x = str(x)

    x = "".join(sorted(list(x)))
    x2 = x[::-1]
    #print("----", x, x2)
    if base != 10:
        result = x_to_dec(x2, base) - x_to_dec(x, base)
        result = dec_to_x(result, base)
    else:
        result = int(x2) - int(x)
        
    result = str(result)
    if len(result) < len(x):
        y = ""
        for t in range(len(x) - len(result)):
            y += "0"
        result = y + result

    return result

def iterkap(x, base= 10):
    """Just for show"""
    for d in range(20):
        x = kap(x, base)

        print(x)


def findkap(n, base=10):
    """finds patterns of kaprekar numbers
    returns the lowest one first(so it's uniform)"""

    primes = (1, 2, 3, 4, 5, 7, 11, 13)
    xlist = []
    for x in range(300):
        n = kap(n, base)
        xlist.append(n)

    xlist = xlist[-100:-1]
    #print(xlist)

    result = None
    for p in range(1, 40):
        if xlist[p] == xlist[2*p] and xlist[p+1] == xlist[2*p + 1] \
        and xlist[p+2] == xlist[2*p +2]:
            result= xlist[p:2 * p]
            break
    if result == None:
        return "NO PATTERN"
    else:
        while result[0] != min(result):
            result.append(result.pop(0))

        return result







        
