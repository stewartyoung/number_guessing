from fractions import Fraction
from math import log

def F(n):
    if n==0: return 0
    lg = int(log(n,2))
    return 1 + Fraction(1,n)*((n+1)*lg - 2*(2**lg-1))

print (F(1000))
