# Last updated: 27/03/2025, 12:55:05
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a list for courses to store prereq's
        prereq = {c : [] for c in range(numCourses)}
        # Populate the list with prereq's
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        # To store the order of courses
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            # Cycle Detected
            if crs in cycle:
                return False
            # Already visited
            if crs in visit:
                return True
            # Adding to cycle set to detect cycle 
            cycle.add(crs)
            # Check all the prereq's of that course
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            # No cycle detected so remove crs from cycle set
            cycle.remove(crs)
            # Add to visit set to avoid calling dfs on it again
            visit.add(crs)
            # Add the crs to the output list
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output