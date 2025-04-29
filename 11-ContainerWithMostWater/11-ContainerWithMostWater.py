# Last updated: 29/04/2025, 00:51:31
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force
        # Find a way to calculate the water stored for each of the container length
        # Store it in a result variable
        # Update the result variable if we find a higher amount of water

        # Two pointer approach makes it more optimal
        # The amount of water stored is equal to height of the smallest bar of the two

        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            water_stored = min(height[l], height[r]) * (abs(l - r))
            res = max(res, water_stored)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res    
