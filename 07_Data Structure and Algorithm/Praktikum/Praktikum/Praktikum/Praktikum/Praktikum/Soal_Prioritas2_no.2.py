def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_rectangle(height, width, start):
    primes = []
    num = start + 1
    while len(primes) < height * width:
        if is_prime(num):
            primes.append(num)
        num += 1
    print(f'Prime rectangle {height}x{width} starting at {start}:')
    print("=====================================")

    for i in range(0, len(primes), width):
        print(' '.join(map(str, primes[i:i+width])))
    print(sum(primes))

prime_rectangle(2, 3, 13) 
prime_rectangle(5,2,1)