"""
    For verification, use: https://www.calculatorsoup.com/calculators/math/prime-factors.php
"""
import os
import time
from numpy import loadtxt


def load_prime_numbers():
    """ Read the pre-created PrimeNumbers.txt from the project root,
        return its contents in an integers list
    Returns:
        [list]: a list of integers, which are read from the PrimeNumbers.txt file
    """
    print('Loading prime numbers...')
    path_to_primes_file = f'{os.getcwd()}{os.sep}PrimeNumbers.txt'
    primes = list(loadtxt(path_to_primes_file, dtype=str, comments="#", delimiter=", ", unpack=False))
    return [int(p) for p in primes]

def find_prime_factors(users_number, prime_numbers):
    # If n happens to be prime then that prime factor is n itself.
    # If n is not prime then it has a prime factor less than itself.
    result = []
    for prime_number in prime_numbers:
        if prime_number > users_number:
            break
        if users_number % prime_number == 0:
            result.append(prime_number)
    return result

def print_prime_factors(prime_factors):
    if not prime_factors:  # if there is no prime factor found
        print('no prime factor found')
    else:
        for prime_factor in prime_factors:
            print(f'Prime factor found: {prime_factor}')

def get_requested_numbers(path_to_calculations):
    """
    If  path_to_calculations is '/home/hakan/Python/PrimeNumbers/Calculations.txt', which has the following lines:

    10, 2, 5
    7, 7
    26541, 3, 983

    then the first number in each line is interpreted as the users_number (e.g. 10, 7, 26541)
    the numbers following the users numbers are the prime factors (e.g. 3, 983 for users_number 26541)

    This function returns in calculated_numbers as a dict:
        calculated_numbers = {
            10: [2, 5],
            7: [7],
            26541: [3, 983]
        }

    Returns:
        dictionary: a dictionary, where each key is the users_number and
        each value is a list containing prime factors
    """
    calculated_numbers = {}
    path_to_calculations = f'{os.getcwd()}{os.sep}Calculations.txt'
    with open(path_to_calculations, 'r') as previous_calculations_file:
        for line in previous_calculations_file:
            if line != '\n':  # if we did not reach end of file
                calculation = [int(s) for s in line.split(', ')]
                users_number = calculation[0]
                calculated_numbers[users_number] = calculation[1:]  # calculation[1:] are prime factors for users_number
    return calculated_numbers

def write_to_file(calculated_numbers):
    """
    Writes calculated numbers into Calculations.txt sitting on the project root

    An example of calculated_numbers:
        calculated_numbers = {
            10: [2, 5],
            7: [7],
            26541: [3, 983]
        }

    For each key/value pairs in calculated_numbers (e.g. 26541: [3, 983])
        Write every number in the pair (e.g. 26541, 3, 983) seperated by ', ' into Calculations.txt
    Args:
        calculated_numbers (dict): contains a key representing the users_number
        and the value, which is a list contianing the prime factors
    """
    with open(path_to_calculations, 'w') as calculations_file:
        for key, value in calculated_numbers.items():
            calculation_row = str([key, *value]).strip('[]') + '\n'
            calculations_file.write(calculation_row)

if __name__ == '__main__':
    path_to_calculations = f'{os.getcwd()}{os.sep}Calculations.txt'
    prime_numbers = load_prime_numbers()
    calculated_numbers = get_requested_numbers(path_to_calculations)
    max_allowed_number = prime_numbers[len(prime_numbers)-1]
    exiting = False
    while not exiting:
        # If a number n>1 is not prime, then it has a prime factor
        # Every integer n>1 has a prime factor.
        users_number = int(input(f'Give me a number between 2 and {max_allowed_number}: '))
        start_time = time.time()
        if users_number in calculated_numbers:  # if we already calculated the prime factors in a previous iteration
            prime_factors = calculated_numbers[users_number]
        else:
            prime_factors = find_prime_factors(users_number, prime_numbers)
            calculated_numbers[users_number] = prime_factors
        print_prime_factors(prime_factors)
        stop_time = time.time()
        calculation_time = stop_time - start_time
        print(f'It took', '%.20f' % calculation_time, 'seconds to find those')
        yes_or_no = input('Do you want to have another iteration? (Y/N): ')
        exiting = False if yes_or_no in ['Y', 'y'] else True
    # at this point, we have a dictionary of calculated_numbers, save them to Calculations.txt for future use.
    write_to_file(calculated_numbers)

