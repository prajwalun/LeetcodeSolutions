# Last updated: 18/06/2025, 18:34:17
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
            heapq.heappush(heap,(freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            freq, num = heapq.heappop(heap)
            result.append(num)
        return result

