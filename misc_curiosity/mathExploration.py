# Why a field must have prime order?

prime = 12
for k in (1, 3, 7, 13, 18):
    print([k*i % prime for i in range(prime)])
print('sorted:')
for k in (1, 3, 7, 13, 18):
    print(sorted([k*i % prime for i in range(prime)]))

# No matter what k you choose, as long as it’s
# greater than 0, multiplying the entire set by k will result in the same
# set as you started with.

# Intuitively, the fact that we have a prime order results in every ele‐
# ment of a finite field being equivalent. If the order of the set was a
# composite number, multiplying the set by one of the divisors would
# result in a smaller set.

for prime in (7, 11, 17, 31):
    print([pow(i, prime-1, prime) for i in range(1, prime)])
 