# infinite loop fixed

def is_power_of_two(n):
# Check if the number can be divided by two without a remainder
  if n <=0:
    return False
  while n % 2 == 0:
    n = n / 2
# If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  
print(is_power_of_two(1024))
print(is_power_of_two(99))