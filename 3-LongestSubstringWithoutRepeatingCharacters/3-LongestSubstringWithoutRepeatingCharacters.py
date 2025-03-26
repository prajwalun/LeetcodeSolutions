# Last updated: 25/03/2025, 23:51:33
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        # Sliding Window
        l = 0
        res = 0
        for r in range(len(s)):
            # Check if char in set
            while s[r] in charSet:
                # Remove the duplicate char
                charSet.remove(s[l])
                # Update window
                l += 1
            charSet.add(s[r])
            # Update result
            res = max(res, r - l + 1)
        return res
                

        