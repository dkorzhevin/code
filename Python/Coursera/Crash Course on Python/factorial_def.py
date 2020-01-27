def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120