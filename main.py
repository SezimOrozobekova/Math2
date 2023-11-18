import math
n, a, error, i = 2, 9, 1e-6, 1
a1 = pow(n, math.floor(math.log(9, 2)))
dif, a2, result = a - a1, 1, 0
x = dif / a1
while abs(math.log(2, 9) - (3+result)) > error:
    result += (((-1) ** (i + 1)) * (1 / math.log(2))) / i * (x ** i)
    i = i + 1
    print(math.log(2, 9))
