# Last updated: 24/04/2025, 12:36:22
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
        # TC: O(n), SC: O(n)
        elements = set()
        for num in nums:
            if num in elements:
                return True
            else:
                elements.add(num)
        return False