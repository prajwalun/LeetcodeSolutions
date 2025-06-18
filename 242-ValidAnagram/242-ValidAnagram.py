# Last updated: 18/06/2025, 13:55:49
from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Using built in sort
        # # return sorted(s) == sorted(t)

        # # Using hash map count
        # # TC: O(n) + O(n) + O(1)
        # # SC: O(k)  where k is number of elements 
        # if len(s) != len(t):
        #     return False
        # # for i in range(len(s)):
        # #     countS[s[i]] = 1 + countS.get(s[i], 0)
        # #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # countS = Counter(s)
        # countT = Counter(t)

        # if countS == countT:
        #     return True
        # return False



        # COunter

        if len(s) != len(t):
            return False
        
        if Counter(s) == Counter(t):
            return True
        return False
    














        

