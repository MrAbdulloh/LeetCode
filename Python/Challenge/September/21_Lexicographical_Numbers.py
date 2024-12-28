# def lexicalOrder(n: int) -> list[int]:
#     result = []
#
#     def dfs(current):
#         if current > n:
#             return
#         result.append(current)
#
#         for i in range(10):
#             next_num = current * 10 + i
#             if next_num > n:
#                 return
#             dfs(next_num)
#
#     for i in range(1, 10):
#         dfs(i)
#
#     return result

def lexicalOrder(n: int) -> list[int]:
    result = []
    num = 1
    for _ in range(n):
        result.append(num)
        if num * 10 <= n:
            num *= 10
        else:
            if num >= n:
                num //= 10
            num += 1
            while num % 10 == 0:
                num //= 10
    return result


n = 13
print(lexicalOrder(n))
