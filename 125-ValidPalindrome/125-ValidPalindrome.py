# Last updated: 28/04/2025, 22:52:43
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
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.alnum(s[l]):
                l += 1
            while r > l and not self.alnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                    return False
            l += 1
            r -= 1
        return True


    def alnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

