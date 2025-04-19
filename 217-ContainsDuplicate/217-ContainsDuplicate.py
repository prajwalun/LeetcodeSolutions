# Last updated: 18/04/2025, 18:11:27
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # TC: O(nlogn) + O(n)
        # SC: O(1)

        # Optimal

        elements = set()
        for i in range(len(nums)):
            if nums[i] in elements:
                return True
            elements.add(nums[i])
        return False