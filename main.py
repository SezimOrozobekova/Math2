import math
import mpmath
n = 2
a = 9
error = 1e-6


a_low = 8
a2 = 8
x = a - a2
before = 1/a2
k = -1
result = mpmath.mpf(0)
i = 1
s_n = mpmath.log(a2, n)


while abs(math.log(a, n) - s_n) > error:
    if i == 1:
        result = round(before * mpmath.log(n) ** k, 6)
        s_n = s_n + result / mpmath.factorial(i) * (x ** i)
    else:
        result = round(before * k * (mpmath.log(n) ** (k-1)) * (1/n), 6)
        s_n = s_n + result / mpmath.factorial(i) * (x ** i)
        before = before * k * (1 / n)
        k = k - 1
    i = i + 1
    print("Derivative of", i, "is", result)
    print("Sum of Teylor series is", s_n)
