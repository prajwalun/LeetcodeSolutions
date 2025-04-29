# Last updated: 28/04/2025, 22:39:15
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]
