"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError
    list.append(2)
    counter = 3
    while len(list) is not number_of_primes:
        common_factor = 0
        for i in range(2, counter+1):
            if counter % i == 0:
                common_factor += 1
        if common_factor == 1:
            list.append(counter)
        counter += 1
    return list
