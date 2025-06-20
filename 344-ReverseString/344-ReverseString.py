# Last updated: 19/06/2025, 18:48:46
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Steps
        # Initialise two pointer variables
        # Use a while loop and compare the l and r element and replace each other
        # Maybe do this using a temp variable
        l, r = 0, len(s) - 1
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l += 1
            r -= 1