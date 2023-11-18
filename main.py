import math
n = 2
a = 9
error = 1e-6


a_low = 8
a2 = 1
diff = a - a_low
x = diff / a_low
before = 1/a2
k = -1
result = 0
i = 1
s_n = math.log(a2, n)

while abs(math.log(a, n) - s_n) > error:
    if i == 1:
        result = round(before * math.log(n) ** k, 6)
        s_n = s_n + result / math.factorial(i) * (x ** i)
        s_n = s_n * 3
    else:
        result = round(before * k * (math.log(n) ** (k-1)) * (1/n), 6)
        s_n = s_n + result / math.factorial(i) * (x ** i)
        s_n = s_n * 3
        before = before * k * (1 / n)
        k = k - 1
    i = i + 1
    print("Derivative of", i, "is", result)
    print("Sum of Teylor series is", s_n)
