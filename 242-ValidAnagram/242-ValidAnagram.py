# Last updated: 24/04/2025, 12:50:55
from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using built in sort
        # return sorted(s) == sorted(t)

        # Using hash map count
        # TC: O(n) + O(n) + O(1)
        # SC: O(k)  where k is number of elements 
        if len(s) != len(t):
            return False

        countS = Counter(s)
        countT = Counter(t)

        if countS == countT:
            return True
        return False

