class Solution(object):
    def isPalindrome(self, x):
        xx = list(str(x))
        if xx == xx[::-1]:
            return True
        else:
            return False


S = Solution()
print(S.isPalindrome(-1.0))
