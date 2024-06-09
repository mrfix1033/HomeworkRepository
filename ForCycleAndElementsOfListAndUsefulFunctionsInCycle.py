numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
mask = [all((i % o for o in range(2, int(i ** .5 + 1)))) if i > 1 else None for i in numbers]
primes = [numbers[p] for p in range(len(numbers)) if mask[p]]
not_primes = [numbers[p] for p in range(len(numbers)) if mask[p] is not None and not mask[p]]
print(primes)
print(not_primes)
