from utils import *
import math
import cmath


def ndiff(f, n):
    if n == 0:
        return f
    else:
        return ndiff(f.diff(), n - 1)
    
def maclaurin_poly(f, n):
    '''
    finds the maclauring series polynmial of f(x) of degree n
    '''
    return poly([ndiff(f, i)(0) / math.factorial(i) for i in range(n + 1)])
def maclaurin_arr(f, n):
    '''
    finds the maclauring series polynmial of f(x) of degree n
    '''
    return [ndiff(f, i)(0) / math.factorial(i) for i in range(n + 1)]

def pade_approx(f, n, m):
    '''
    finds the pade approximant n/m for f(x)
    '''
    arr = maclaurin_arr(f, n + m)
    numerator_arr = [[arr[n - m + i + j + 1] for j in range(m + 1)] for i in range(m)]
    sub_arr = []
    for k in range(m + 1):
        x = poly([0, 1])
        new_poly = sum([arr[i - m + k] * x**i for i in range(m-k, n + 1)])
        sub_arr.append(new_poly)
    
    numerator_arr.append(sub_arr[:])
    
    denom_arr = [[arr[n - m + i + j + 1] for j in range(m + 1)] for i in range(m)]
    sub_arr = []
    for k in range(m + 1):
        x = poly([0, 1])
        sub_arr.append(x ** (m - k))
    
    denom_arr.append(sub_arr[:])

    num = matrix(numerator_arr).det()
    denom = matrix(denom_arr).det()
    return rexp_poly(num, denom)

def rexp_simplification(r, interval=[-1, 1]):
    err, n = None, 0
    for d in range(abs(r.p1.deg - r.p2.deg) + 1):
        f = pade_approx(r, r.p1.deg - d, r.p2.deg - d)
        nn, new_err = d, numericIntegration(lambda x : (f(x) - r(x))**2, interval[0], interval[1], dx=0.01)
        if err is None:
            err, n = new_err, nn
        elif new_err < err:
            err, n = new_err, nn
    
    return pade_approx(r, r.p1.deg - n, r.p2.deg - n)
