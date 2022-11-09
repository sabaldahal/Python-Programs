
import doctest
import math


def egypt(p, q, output=True):
    """ Uses Greedy approach to print out a listing
    representing a sum of unit fractions,
    with sum equal to p/q

    >>> egypt(3,4)
    '1/2 + 1/4 = 3/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12 = 11/12'
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112 = 123/124'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424 = 103/104'

    """
    "***code here***"

    strorg = ("{0}/{1}").format(p, q)
    if p == 1 or q % p == 0:
        a = q // p
        strcpy = ("1/{0}" .format(a))
        return strcpy
    elif p == 0 or q == 0:
        return
    else:
        if output:
            a = math.ceil(q/p)
            strcpy = ("1/{0}" .format(a))
            return strcpy + " + " + (egypt((p*a) - q, q*a, output=False)) + " = " + strorg
        else:
            a = math.ceil(q/p)
            strcpy = ("1/{0}" .format(a))
            return strcpy + " + " + egypt((p*a) - q, q*a, output=False)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
