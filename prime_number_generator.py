import primesieve
import os

def write_to_file(primes, append_comma, primes_file):
    content = str(list(primes))
    content = content.strip('[]')
    content = content + ', ' if append_comma else content
    primes_file.write(content)

def generate_prime_numbers(max_limit, primes_file):
    result = []
    from_limit = 1
    iteration = 1
    while True:
        to_limit = (from_limit + 100) if (max_limit > (from_limit + 100)) else max_limit
        result += list(primesieve.primes(from_limit, to_limit))
        print(f'Calculated from {from_limit} to {to_limit}, max({max_limit})')
        iteration+=1
        finished = to_limit == max_limit
        if iteration == 10 or finished:
            print('Writing to file...')
            write_to_file(primes=result, append_comma = not finished, primes_file=primes_file)
            iteration = 1
            result = []
        if to_limit == max_limit:
            break
        from_limit = to_limit+1

if __name__ == '__main__':
    path_to_primes_file = f'{os.getcwd()}{os.sep}PrimeNumbers.txt'
    with open(path_to_primes_file, 'w') as primes_file:
        generate_prime_numbers(max_limit=99999999, primes_file=primes_file)

