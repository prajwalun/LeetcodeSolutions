# Last updated: 18/04/2025, 18:15:32
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)