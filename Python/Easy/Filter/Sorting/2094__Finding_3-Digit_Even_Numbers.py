from itertools import permutations


def findEvenNumbers(digits: list[int]) -> list[int]:
    unique_numbers = set()

    for perm in permutations(digits, 3):
        num = perm[0] * 100 + perm[1] * 10 + perm[2]

        if perm[0] != 0 and perm[2] % 2 == 0:
            unique_numbers.add(num)
    return sorted(unique_numbers)

digits = [2, 1, 3, 0]
print(findEvenNumbers(digits))
