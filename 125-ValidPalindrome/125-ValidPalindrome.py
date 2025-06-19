# Last updated: 19/06/2025, 12:25:05
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Extra Space with new_str and also generating the reverse or new_str
        # if not s:
        #     return False
        # new_str = ''
        # for c in s:
        #     if c.isalnum():
        #         new_str += c.lower()
        # return new_str == new_str[::-1]

        # Optimal without extra space
        # Two Pointers

        if not s:
            return False
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

    def alnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

