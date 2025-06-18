# Last updated: 18/06/2025, 13:38:13
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Optimal

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False