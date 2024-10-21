def ReduceANumberToZero(n):
    i = 0
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            i = i + 1
        else:
            n = n - 1
            i = i + 1
    return i

result = ReduceANumberToZero(123)
print(result)