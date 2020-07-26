def is_it_prime(n):
    if n < 2:
        return 0
    if n > 2 and n % 2 == 0:
        return 0
    if n == 2:
        return 1
    for d in range(3, n//2):
        if n % d == 0:
            return 0
    return 1
    

def next_prime_number(n):
    if is_it_prime(n):
        n += 1
    while is_it_prime(n) == 0:
        n += 1
    return n

n = 0
n = int(input('Write a number so that I can give you the first prime number larger than it: '))
print (next_prime_number(n))