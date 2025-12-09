def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def list_format(primes):
    return primes

def column_format(primes):
    return '\n'.join(str(prime) for prime in primes)

def count_format(primes):
    return len(primes)

def find_primes(n, output_format):
    if output_format == 'list':
        return list_format(generate_primes(n))
    elif output_format == 'column':
        return column_format(generate_primes(n))
    elif output_format == 'count':
        return count_format(generate_primes(n))

print(find_primes(20, 'list'))
print('-' * 20)
print(find_primes(20, 'column'))
print('-' * 20)
print(find_primes(20, 'count'))