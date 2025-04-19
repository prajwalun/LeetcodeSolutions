# Last updated: 18/04/2025, 18:24:57
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using built in sort
        # return sorted(s) == sorted(t)

        # Using hash map count
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT