from pwn import process, remote
from sage.all import divisors, is_pseudoprime, factor
from Crypto.Util.number import long_to_bytes
import math


ct = 611142254405063827592801146302447289406583406739037319967831929495820356540197143799949439570575545193567545373382063508745891664959358452805982104434526
e = 0x10001
phi = 5766519321732303614602774063039817994229059369350942586704472004284400792639050641102051094143465282172553506082870684687445379400436177178525327208209136
d = pow(e,-1,phi)
kphi = e * d - 1

print(e * d - 1)
factors = [2,2,2,2 , 11 , 53 , 1231 , 3011 , 6311 , 29927 , 42764336533 , 6092059936124221]



filteredfactors = []
for i in factors:
    if math.log2((e * d - 1)//i) < 508: break
    filteredfactors.append(i)


print(filteredfactors)


possk = set()
for i in range(2**len(filteredfactors)):
    currk = 1
    for j in range(len(filteredfactors)):
        if (i & (1<<j)) != 0:
            currk *= filteredfactors[j]
    if int(math.log2((e * d - 1)//currk)) <= 257 and int(math.log2((e * d - 1)//currk)) >= 254:
        possk.add(currk)


print(possk)