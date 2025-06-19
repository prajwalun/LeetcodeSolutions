# Last updated: 18/06/2025, 20:43:54
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * (len(nums))

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res

        # Make all the elements 1 in the res arr
        res = [1] * (len(nums))
        # Set the first prefix which is 1
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res