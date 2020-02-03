def sum_divisors(n):
    dividor =1
    result = 0
    while dividor < n :
        if n % dividor == 0:
            result = result + dividor
        dividor += 1
    return result


print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16