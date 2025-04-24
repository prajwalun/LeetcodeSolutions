# Last updated: 24/04/2025, 14:16:25
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force approach
        # Sort the elements and return the last k elements
       
        # count = Counter(nums)
        # sort_freq = sorted(count, key=count.get)
        
        # return sort_freq[-k:]

        # Optimal approach
        # Use a heap to store the elements and pop k elements from it

        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heap.append((-freq, num))
        heapq.heapify(heap)

        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res
        

