""" Functions to calculate a list of prime numbers """
# Regular primes


def list_regular_primes(quantity):
    """ Return a list with the required quantity of prime numbers """
    limit = quantity
    list_primes = range_regular_primes(quantity, None, None, None)
    while len(list_primes) < limit:
        start = quantity + 1
        quantity = quantity + int(quantity / 2)
        end = quantity
        list_primes = range_regular_primes(quantity, start, end, list_primes)

    list_primes = list_primes[0:limit]
    return list_primes


def range_regular_primes(quantity, start, end, list_temp):
    """ Return a list with the prime numbers from a range  """
    if start is None:
        range_primes = []
        for num in range(2, quantity):
            prime = True
            for i in range(2, num):
                if (num % i == 0):
                    prime = False
            if prime:
                range_primes.append(num)
        return range_primes
    else:
        for num in range(start, end):
            prime = True
            for i in range(2, num):
                if (num % i == 0):
                    prime = False
            if prime:
                list_temp.append(num)
        return list_temp


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
