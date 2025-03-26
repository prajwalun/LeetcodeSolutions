# Last updated: 26/03/2025, 15:53:57
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a map to store prereq's
        preMap = {i : [] for i in range(numCourses)}
        # Appending the prereq to its associated course
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # Mark the visited course with a set
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Course already exists and there's a loop
                return False
            if preMap[crs] == []:
                return True

            # Add course to set
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # If successful remove the crs from visiting set, update preMap for that crs and return True
            visiting.remove(crs)
            preMap[crs] = []
            return True
        
        # Go through all the courses
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                
