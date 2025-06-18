# Last updated: 18/06/2025, 14:01:02
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



        # Using hashmap count

        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True

       
    














        

