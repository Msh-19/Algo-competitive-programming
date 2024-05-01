# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def count_almost_primes(n):
    distinct_prime_divisors_count = [0] * (n + 1)

    for i in range(2, n + 1):
        if distinct_prime_divisors_count[i] == 0:
            for j in range(i, n + 1, i):
                distinct_prime_divisors_count[j] += 1

    almost_prime_count = sum(1 for count in distinct_prime_divisors_count if count == 2)

    return almost_prime_count

n = int(input())


print(count_almost_primes(n))
