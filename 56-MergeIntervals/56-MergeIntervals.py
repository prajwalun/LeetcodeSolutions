# Last updated: 26/03/2025, 17:12:16
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals
        intervals.sort(key= lambda x: x[0])
        # Add the first interval to the merged list
        merged = [intervals[0]]
        # Loop from the 1st index because the 0th is already in the merged list
        for curr in intervals[1:]:
            # Add the last interval in the merged list to prev
            prev = merged[-1]

            # Check overlap
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(curr)

        return merged



