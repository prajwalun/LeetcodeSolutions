# Last updated: 22/06/2025, 19:11:04
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # only add open parentheses if open < n
        # only add a closing parenthes if closed < open
        # valid if open == closed == n
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
