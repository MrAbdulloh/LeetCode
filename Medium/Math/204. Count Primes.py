def countPrimes(n: int) -> int:
    if n <= 2:
        return 0

    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i:n:i] = [False] * len(primes[i * i:n:i])

    return sum(primes)

# ## 1 method ERROR RUN TIME
# def countPrimes(self, n: int) -> int:
#     def is_primes(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     count = 0
#     for i in range(2, n):
#         if is_primes(i):
#             count += 1
#     return count
#
#
# ##  2 method ERROR RUN TIME
# def countPrimes(self, n: int) -> int:
#     def is_primes(num):
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#         return is_prime
#
#     count = 0
#     for i in range(2, n):
#         if is_primes(i):
#             count += 1
#     return count
