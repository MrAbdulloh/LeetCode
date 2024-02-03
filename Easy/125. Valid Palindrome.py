"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""


### first method

# def isPalindrome(s: str) -> bool:
#     """
#     :type s: str
#     :rtype: bool
#     """
#     result_s = ''.join(char for char in s if char not in [' ', ',', '.', ':']).lower()
#
#     return result_s[::-1] == result_s

### second method

# def isPalindrome(s: str) -> bool:
#     filterd = ''.join(filter(str.isalnum, s)).lower()
#     return filterd == filterd[::-1]
#
#
# text = 'race a car'
# # text = ''
# print(isPalindrome(text))


### third method

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while right < left:
            while right < left and not self.isPalindrome(s[left]):
                left += 1

            while left < right and not self.isPalindrome(s[right]):
                right -= 1
            if s[left].lower() == s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isalphanum(self, s: str) -> bool:
        return (
                ord('0') <= ord(s) <= ord('9')
                or
                ord('A') <= ord(s) <= ord('Z')
                or
                ord('a') <= ord(s) <= ord('z')
        )
