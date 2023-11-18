import math
n, a, error, i = 2, 8.9991, 1e-6, 1
a1 = pow(n, math.floor(math.log(a, 2)))
dif, a2, result = a - a1, 1, 0
x = dif / a1
while abs(math.log(a, 2) - (math.log(a1, 2) + result)) > error:
    result += (((-1) ** (i + 1)) * (1 / math.log(2))) / i * (x ** i)
    i = i + 1
print(result + math.log(a1, 2))
