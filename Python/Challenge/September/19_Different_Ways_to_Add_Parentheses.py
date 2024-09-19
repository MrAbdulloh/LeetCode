# def diffWaysToCompute(expression: str) -> list[int]:
#     if expression.isdigit():
#         return [int(expression)]
#     result = []
#
#     for i, char in enumerate(expression):
#         if char in '+-*':
#             left = diffWaysToCompute(expression[:i])
#             right = diffWaysToCompute(expression[i + 1:])
#
#             for l in left:
#                 for r in right:
#                     if char == '+':
#                         result.append(l + r)
#                     elif char == '-':
#                         result.append(l - r)
#                     elif char == '*':
#                         result.append(l * r)
#     return result
#
#
# expression = "2-1-1"
# print(diffWaysToCompute(expression))

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if expression.isdigit():
            return [int(expression)]
        result = []

        for i, char in enumerate(expression):
            if char in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:
                        if char == '+':
                            result.append(l + r)
                        elif char == '-':
                            result.append(l - r)
                        elif char == '*':
                            result.append(l * r)

        return result


s = Solution()
print(s.diffWaysToCompute("2-1-1"))