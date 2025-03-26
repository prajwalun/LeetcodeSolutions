# Last updated: 25/03/2025, 22:11:48
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid or not grid[0]:
        #     return 0
        
        # rows = len(grid)
        # cols = len(grid[0])
        # islands = 0
        
        # def dfs(row, col):
        #     if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
        #         return
        #     grid[row][col] = '0'  # Mark current cell as visited
            
        #     # Recursively visit all four possible directions
        #     dfs(row - 1, col)  # Up
        #     dfs(row + 1, col)  # Down
        #     dfs(row, col - 1)  # Left
        #     dfs(row, col + 1)  # Right
        
        # # Traverse each cell in the grid
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == '1':
        #             # Found a new island, initiate DFS to mark all connected land cells
        #             dfs(row, col)
        #             islands += 1
        
        # return islands


        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        # DFS logic
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
                return
            # Marked as visited
            grid[row][col] = 0

            # Recursive check on all directions of the current cell
            dfs(row - 1, col) # Up
            dfs(row + 1, col) # Down
            dfs(row, col - 1) # Left
            dfs(row, col + 1) # Right

        # Traverse each cell
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                # Call DFS on the island
                    dfs(row, col)
                # Increment island count
                    islands += 1
        
        return islands



        