# Last updated: 18/06/2025, 14:30:48
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force - TC: O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         currSum = nums[i] + nums[j]
        #         if currSum == target:
        #             return [i,j]

        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i

        
                






        # #Optimized to O(n) 
        prevMap = {} #value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


      