# Prime number sieve with generators

import itertools
from typing import Iterator


def iter_primes() -> Iterator[int]:
    # an iterator of all numbers between 2 and +infinity
    numbers = itertools.count(2)  # type: Iterator[int]

    # generate primes forever
    while True:
        # get the first number from the iterator (always a prime)
        prime = next(numbers)
        yield prime

        # this code iteratively builds up a chain of
        # filters...slightly tricky, but ponder it a bit
        numbers = filter(prime.__rmod__, numbers)

for p in iter_primes():
    if p > 1000:
        break
    print(p)
