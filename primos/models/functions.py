""" Functions to calculate a list of prime numbers """
# Regular primes


def list_regular_primes(quantity):
    """ Return a list with the required quantity of prime numbers """
    limit = quantity
    list_primes = range_regular_primes(quantity)
    while len(list_primes) < limit:
        quantity = quantity + int(quantity / 2)
        list_primes = range_regular_primes(quantity)

    list_primes = list_primes[0:limit]
    return list_primes


def range_regular_primes(quantity):
    """ Return a list with the prime numbers from a range  """
    range_primes = []
    for num in range(2, quantity):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            range_primes.append(num)
    return range_primes


# Pair prime twins
def list_twins_primes(quantity):
    """ Return a list with the required quantity of pairs of twins prime numbers """
    limit = quantity
    list_pair = range_twins_primes(quantity)
    while len(list_pair) < limit:
        quantity = quantity + int(quantity / 2)
        list_pair = range_twins_primes(quantity)
    list_pair = list_pair[0:limit]
    return list_pair


def range_twins_primes(quantity):
    """ Return a list with pairs of twins prime numbers from a range  """
    list_pair = []
    n = 2
    prime = []
    noesprimo = []

    while n <= quantity:
        if n not in noesprimo:
            prime.append(n)

            for i in range(n*2, quantity+1, n):
                noesprimo .append(i)
        n += 1
    for p in prime:
        if p+2 in prime:
            list_pair.append([p, p+2])
    return list_pair
