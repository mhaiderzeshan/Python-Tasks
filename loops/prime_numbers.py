"""
Write a program that finds all prime numbers within a range using the Sieve
of Eratosthenes algorithm.
"""


n = int(input("Enter the number: "))

prime = [True] * (n + 1)
prime[0] = prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False

primes = []
for z in range(n+1):
    if prime[z]:
        primes.append(z)

print(primes)
