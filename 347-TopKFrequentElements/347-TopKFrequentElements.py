# Last updated: 02/04/2025, 13:46:55

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force approach
        # Sort the elements and return the last k elements
       
        count = Counter(nums)
        sort_freq = sorted(count, key=count.get)
        
        return sort_freq[-k:]

