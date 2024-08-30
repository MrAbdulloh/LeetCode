"""
https://leetcode.com/problems/fizz-buzz/
"""


def fizzBuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(f'{i}')
    return result

n = 3
print(fizzBuzz(n))