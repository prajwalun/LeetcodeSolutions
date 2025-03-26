# Last updated: 26/03/2025, 14:26:00
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Get the count of each character and store the key value pair {char : freq}
        count = Counter(s)
        # Populating the maxHeap, make the count negative to act as maxHeap in python
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        # Heapify to get the highest freq on top, sorted the way we want
        heapq.heapify(maxHeap)
        # Store the most freq element in prev
        prev = None
        res = ""
        
        while maxHeap or prev:
            # Condition to make sure we don't add a duplicate char next to each other
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            # Technically supposed to decrement the freq count but since we have the count values as negative, we increment here to deacrese the count
            cnt += 1
            
            # If a freq char count exists, we add it to prev first, process a new char in the heap to avoid duplicate and then push prev to heap again
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            # This is the line where we add the count and char to prev if the freq is not 0
            if cnt != 0:
                prev = [cnt, char]

        return res

            

