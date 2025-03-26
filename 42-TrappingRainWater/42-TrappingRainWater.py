# Last updated: 25/03/2025, 19:00:18
class Solution:

    # Two Pointer Approach

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # Initiliase the variables for the two pointer approach
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        # Two pointer condition
        while l < r:
            # Checking the minimum of each max
            if leftMax < rightMax:
                l += 1
                # Updating max first and then adding to result to avoid negative values
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                # Updating max first and then adding to result to avoid negative values
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res

        # TC: O(n) for the while loop going through the whole height only once, n being the number of elements in the height
        # SC: O(1) for the different pointers used like l, r, rightMax, leftMax and res