from math import gcd # not in fractions module anymore

# least common multiple
def _lcm(a, b):
    return abs(a) * (abs(b) / gcd(a, b))

# simplifies the fraction
def _simplify(frac):
    if frac[1] == 0:
        raise ValueError("denominator cannot be 0!!!")

    frac[0] = int(frac[0])
    frac[1] = int(frac[1])

    if (frac[0] < 0 and frac[1] < 0) or (frac[0] > 0 and frac[1] < 0):
        frac[0] = -frac[0]
        frac[1] = -frac[1]
    
    common_factor = gcd(frac[0], frac[1])
    frac[0] /= common_factor
    frac[1] /= common_factor

    if frac[0] == 0: frac[1] = 1

    return frac

# frac1 + frac2 or frac1 - frac2
def _add_sub_frac(frac1, frac2, op):
    frac3 = [None] * 2
    frac3[1] = _lcm(frac1[1], frac2[1])
    frac3[0] = op(frac1[0] * (frac3[1] / frac1[1]), frac2[0] * (frac3[1] / frac2[1]))
    return _simplify(frac3)

# ====================================================
# ----------------------------------------------------
# ====================================================

# frac1 - frac2
def add_frac(frac1, frac2):
    return _add_sub_frac(frac1, frac2, op=lambda x, y: x + y)  

# frac1 - frac2
def sub_frac(frac1, frac2):
    return _add_sub_frac(frac1, frac2, op=lambda x, y: x - y)        

# frac1 * frac2
def mul_frac(frac1, frac2):
    return _simplify([frac1[0] * frac2[0], frac1[1] * frac2[1]])        

# frac1 / frac2
def div_frac(frac1, frac2):
    return _simplify([frac1[0] * frac2[1], frac1[1] * frac2[0]])       

# bool, czy dodatni
def is_positive(frac):
    return ((frac[0] * frac[1]) > 0)          

# bool, typu [0, x]
def is_zero(frac): 
    return (frac[0] == 0)

# -1 | 0 | +1
def cmp_frac(frac1, frac2): 
    f1 = frac2float(frac1)
    f2 = frac2float(frac2)
    if f1 > f2: return -1
    elif f1 == f2: return 0
    else: return 1

def frac2float(frac):
    return (frac[0] / frac[1])

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)
