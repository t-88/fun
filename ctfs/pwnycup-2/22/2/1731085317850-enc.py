from Crypto.Util.number import long_to_bytes, bytes_to_long, size, inverse
from math import gcd, prod
import operator
from functools import reduce
import itertools



ct = 611142254405063827592801146302447289406583406739037319967831929495820356540197143799949439570575545193567545373382063508745891664959358452805982104434526
e = 0x10001
phi = 5766519321732303614602774063039817994229059369350942586704472004284400792639050641102051094143465282172553506082870684687445379400436177178525327208209136
d = pow(e,-1,phi)

def parse_pow(x):
    r = x.split('^')
    if len(r) == 1:
        return [int(r[0])]
    else:
        return [int(r[0])] * int(r[1])

print(phi)

print('insert factors (use https://www.alpertron.com.ar/ECM.HTM) -- make sure to replace powers with "^":')
factors_in = input()
factors = "2^4 x 11 x 53 x 1231 x 3011 x 6311 x 29927 x 42764336533 x 6092059936124221 x 101440719170155015909064471710144683792396347074627934583192001895065326571520084031205462517111902300805427284059"

from Crypto.Util.number import long_to_bytes

from Crypto.Util.number import long_to_bytes, bytes_to_long, size, inverse
from math import gcd, prod
import operator
from functools import reduce
import itertools



ct = 611142254405063827592801146302447289406583406739037319967831929495820356540197143799949439570575545193567545373382063508745891664959358452805982104434526
e = 0x10001
phi = 5766519321732303614602774063039817994229059369350942586704472004284400792639050641102051094143465282172553506082870684687445379400436177178525327208209136


d = pow(e,-1,phi)


print(e*d -1 )


from Crypto.Util.number import isPrime, long_to_bytes
from string import ascii_letters, digits
from itertools import combinations
from sympy import divisors
from math import log2



primes = [x + 1 for x in ds if isPrime(x + 1)]
correct_size_primes = [x for x in primes if log2(x) // 1 == 127]

valid_plaintexts = []
charset = ascii_letters + digits
for p, q in combinations(correct_size_primes, 2):
    try:
        s = long_to_bytes(pow(phi, d, p * q)).decode("ascii")
        if all([c in charset for c in s]):
            valid_plaintexts.append(s)
    except Exception:
        continue

print(valid_plaintexts)


def get_subsets_sum(data, target, epsilon):
    """Find sums of values in `data` which gives `target` ± `epsilon`."""
    subsets, subsets_primes = [], []

    differences = {}
    for value in data:
        prospects = []
        for diff in differences:
            if (diff >= value) and abs(value - diff) < epsilon:
                new_subset = [value] + differences[diff]
                new_subset.sort()
                if new_subset not in subsets:
                    subsets.append(new_subset)
            if value - diff < 0.:
                prospects.append((value, diff))
 
        # update the differences record
        for prospect in prospects:
            new_diff = target - sum(differences[prospect[1]]) - prospect[0]
            differences[new_diff] = differences[prospect[1]] + [prospect[0]]
        differences[target - value] = [value]
    return subsets

import math

def get_subsets_product(data, target, epsilon):
    """Find products of values in `data` which gives `target` ± `epsilon` (`epsilon` is given as bit size)."""  
    data = sorted(data, reverse=True)
    candidates = []
    bit_sizes = [math.log2(value) for value in data]
    target_bit_size = math.log2(target)
    bit_sizes_substets = get_subsets_sum(bit_sizes, target_bit_size, epsilon)
    for subset in bit_sizes_substets:
        values_subset = [data[bit_sizes.index(bit_size)] for bit_size in subset]
        candidates.append(math.prod(values_subset))
    return candidates


dem1 = d * e - 1

k_size_max = int(math.log2(dem1) - math.log2(ct))
k_factors = list(filter(lambda factor: math.log2(factor) < k_size_max, factors))
k_candidates = get_subsets_product(k_factors, 2**17, 1)
