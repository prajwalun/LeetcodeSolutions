# Last updated: 04/07/2025, 14:35:20
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         res = nums[i] + nums[j]
        #         if res == target:
        #             return [i, j]
        # return []
  
        prevMap = {} # value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
