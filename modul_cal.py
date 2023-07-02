def log(x,base):
    result = ln(x)/ln(base)
    return round(result,4) #I have limited the result bc it does not give exact accuracy.

def ln(x):
    val = x
    return round(99999999*(x**(1/99999999)-1),4)

def fact(x):
    while True:
        f=1
        for i in range(1, x+1):
            f *= i
            i += 1
        return f

def conv(x):
    rad = x *  3.1415926 / 180
    return rad

def abs(x,y):
    if x > y:
       return x-y
    else:
       return y-x

def pow(x,y):
    p = 1
    for i in range(1,y+1):
        p *= x
    return p

def sin(x):
    eps = 0.0001
    n = 2
    i = x
    j = i - ((x**3)*1.0/6)
    while abs(i,j) >= eps:
        i = j
        j += pow(-1, n) * pow(x, 2 * n + 1) * 1.0 / fact(2 * n + 1)
        n = n + 1
    return round(j,4)

def cos(x):
    c = (1-sin(x)**2)**0.5
    return round(c,4)

def tan(x):
    t = sin(x)/cos(x)
    return round(t, 4)
    
def cot(x):
    ct = cos(x)/sin(x)
    return round(ct,4)
