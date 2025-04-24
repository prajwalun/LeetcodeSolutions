# Last updated: 24/04/2025, 13:26:11
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force - TC: O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             return [i,j]

        # #Optimized to O(n) 
        prevMap = {} #value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        

      