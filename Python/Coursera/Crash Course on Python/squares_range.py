def square(n):
    return n*n

#print(square(8))

def sum_squares(x):
    sum = 0
    for n in range(sum,x):
        sum += square(x)
        return square(x)
        x -= 1

print(sum_squares(100))

#print(sum_squares(10)) # Should be 285